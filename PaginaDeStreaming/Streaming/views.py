from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.contrib import  messages
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


def crearmenu(User):
    html = "<a href='/frontpage'>home</a>"
    if User == "superuser":
        html += "<a href='/reporte'>reporte</a>"    
        html += "<a href='/grafico'>grafico</a>"
    elif User == "cliente":
        html +="<a href='/miperfil'>miperfil</a>"
    elif User == "visitante":
        html +="<a href='/login'>login</a>"
    return html        
        

def frontpage(request):
    logged_user = getLoggedUser(request)
    htmlmenu = crearmenu("cliente")
    if logged_user is not None:
        htmlmenu += " " + logged_user
    return render(request, "frontpage.html", {"logged_user": logged_user,"htmlmenu":htmlmenu})

def displaypage(request):
    return render(request, "displaypage.html")

def register(request):
    response = render(request, "register.html")
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Ese nombre de usuario ya existe. Elija otro.")
            return redirect('./')

        if User.objects.filter(email=email).exists():
            messages.error(request, "La dirección de correo electrónico ya existe. Elija otra.")
            return redirect('./')

        if pass1 != pass2:
            messages.error(request, "Las contraseñas ingresadas no coinciden. Ingreselas nuevamente.")
            return redirect('./')

        if not username.isalnum():
            messages.error(request, "El nombre de usuario no puede contener caracteres especiales.")
            return redirect('./')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()

        myusuario = Usuario(email = email, nombre = fname, apellido=lname, password = pass1)
        myusuario.save()
        
        messages.success(request, "Su cuenta fue creada con éxito.")
    return response

def RegistTarjeta(request):
    logged_user = getLoggedUser(request)
    tipoTarjetas = TipoTarjeta.objects.all()
    response = render(request, "Regist_Tarjeta.html", {"tipoTarjetas":tipoTarjetas})
    if request.method == "POST":
        nombres = request.POST['Nombres']
        apellidos = request.POST['Apellidos']
        tarjeta = request.POST['Tarjeta']
        codigo = request.POST['Codigo']
        tipo = request.POST['tipoTarjeta']
        fecha = request.POST['fecha']

        if Tarjeta.objects.filter(numero_tarjeta=tarjeta):
            messages.error(request, "Ese nombre de usuario ya existe. Elija otro.")
            return redirect('./Regist_Tarjeta.html')
        
        if not nombres.isalnum():
            messages.error(request, "Su nombre no puede contener caracteres especiales.")
            return redirect('./Regist_Tarjeta.html')

        tipoTarjeta = TipoTarjeta.objects.get(tipo_tarjeta=tipo)

        mytarjerta = Tarjeta(nombreTitular = nombres, apellidoTitular = apellidos, numero_tarjeta = tarjeta, fecha_vencimiento = fecha, codigo_seguridad = codigo, TipoTarjeta = tipoTarjeta, usuario = logged_user)
        mytarjerta.save()
        
        messages.success(request, "Su cuenta fue creada con éxito.")
    return response

def selecplan(request):
    logged_user = getLoggedUser(request)
    return render(request, 'selecplan.html', {"logged_user": logged_user})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["user"] = username
            return redirect('frontpage.html')
        else:
            messages.success(request, "Las credenciales no coinciden")
            return redirect('login.html')
    return render(request, 'login.html')

def login_fail(request):
    return render(request,"login_fail.html")

def logout(request):
    auth_logout(request)
    return redirect("/")

def getLoggedUser(request: HttpRequest):
    return request.session.get("user")

def contenido(request):
    return render(request,"contenido.html")