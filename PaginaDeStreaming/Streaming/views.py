from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import login
from .forms import CustomAuthenticationForm
from .forms import UsuarioRegister, PlanForm, TarjetaForm
from django.contrib.auth import logout as auth_logout
from django.http import HttpRequest
import datetime

# Create your views here.


def getLoggedUser(request: HttpRequest):
    return request.session.get("user", "Iniciar Se")

def frontpage(request):
    context= {"logged_user": getLoggedUser(request)}
    return render(request, "frontpage.html", context)

def displaypage(request):
    return render(request, "displaypage.html")

def logout(request):
    auth_logout(request)
    return redirect("/")

def planView(request):
    
    formP = PlanForm
    context = {
        'formP': formP
        }
    chunks = {}
    nro = 0
    plan_dict = {}
    cxp = {}
    for i in Plan.objects.all():
        nro = nro +1
        plan_dict = {}
        
        plan_dict.update({"detalle" : i.detalle})

        plan_dict.update({"tipo" : i.tipo_plan})

        plan_dict.update({"id" : i})

        ## despues podemos poner las caracteristicas, solo puse tipo y detalle

        chunks.update({"plan_dict"+nro.__str__(): plan_dict})
        cxp.update({"cxp"+ nro.__str__():CaracteristicasXPlan.objects.filter(plan = i.id)}) 
        
        
    context.update({"cxp": cxp})
    for o,t in cxp.items():
        for k in t:
            if k.plan == "t2":
                print(k)
        
    
    context.update({"chunks" : chunks})
    response = render(request, "plan.html", context)

    if request.method == "POST":
        formP = PlanForm(request.POST)
        if formP.is_valid():
            eleccion = formP.cleaned_data.get("btn")

            for x,y in chunks.items():
                if x == eleccion:
                    response = redirect("/register")
                    
                    idp = Plan.objects.get(detalle =y["detalle"]).id
                    response.set_cookie('Idp',idp)

                    
    
    
    return response

def registerView(request):
    formU = UsuarioRegister
    context = {
        'formU': formU
        }
    response = render(request, "register.html", context)
    if request.method == "POST":
        formU = UsuarioRegister(request.POST)
        if formU.is_valid():
            username = request.POST['username']
            fname = formU['nombre'].value()
            lname = formU['nombre'].value()
            email_tomado = formU['email'].value()
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if User.objects.filter(username=username):
                print("Ese nombre de usuario ya existe. Elija otro.")
                return redirect('/register')

            if User.objects.filter(email=email_tomado).exists():
                print("La dirección de correo electrónico ya existe. Elija otra.")
                return redirect('/register')

            if pass1 != pass2:
                print("Las contraseñas ingresadas no coinciden. Ingreselas nuevamente.")
                return redirect('/register')

            if not username.isalnum():
                print("El nombre de usuario no puede contener caracteres especiales.")
                return redirect('/register')
            
            myuser = User.objects.create_user(username, email_tomado, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.is_active = True
            myuser.save()

            myusuario = Usuario(email = email_tomado, nombre = fname, apellido=lname, password = pass1)
            myusuario.save()
            

            response = redirect("/tarjeta")
            response.set_cookie('Usuario',Usuario.objects.get(email =email_tomado).id)
            messages.success(request, "Su cuenta fue creada con éxito.")
    return response

def loginView(request):
    form = CustomAuthenticationForm
    context = {'form': form}

    response = render(request, 'login.html', context)
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            Usuario = form.get_user()
            login(request, Usuario)
            # Redirige a la página deseada después del inicio de sesión
            return redirect('frontpage.html')
    return response

def tarjetaView(request):
    formT = TarjetaForm
    context = {
        'formT': formT
        }
    response = render(request, "tarjeta.html", context)

    if request.method == 'POST':
        formT = TarjetaForm(request.POST)
        if formT.is_valid():
            nombreTitular_ = formT['nombreTitular'].value()
            apellidoTitular_ = formT['apellidoTitular'].value()
            numero_tarjeta_ = formT['numero_tarjeta'].value()
            fecha_vencimiento_ = formT['fecha_vencimiento'].value()
            codigo_seguridad_ = formT['codigo_seguridad'].value()
            tipoTarjeta_ = TipoTarjeta.objects.get(id = formT['tipoTarjeta'].value()) 
            usuario_ = Usuario(request.COOKIES.get("Usuario"))

            myTarjeta = Tarjeta(nombreTitular = nombreTitular_, apellidoTitular = apellidoTitular_, numero_tarjeta = numero_tarjeta_,fecha_vencimiento = fecha_vencimiento_, codigo_seguridad = codigo_seguridad_, tipoTarjeta = tipoTarjeta_, usuario = usuario_)
            myTarjeta.save()

            sus = Suscripcion(fecha_suscripcion = datetime.date.today(), SusActiva = True, id_tarjeta= Tarjeta.objects.get(numero_tarjeta = numero_tarjeta_) ,id_plan = Plan(request.COOKIES.get('Idp')),id_usuario = Usuario(request.COOKIES.get("Usuario")))
            sus.save()

    return response

def login_failView(request):
    return render(request,"login_fail.html")