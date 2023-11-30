from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import login
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required



def frontpage(request):
    return render(request, "frontpage.html")

@login_required
def selecplan(request):
    if request.method == "GET":
        resultados = list()
        planes = Plan.objects.all()
        for plan in planes:
            resultados.append({
                'plan' : plan,
                'caracteristicas' : CaracteristicasXPlan.objects.filter(plan=plan)
            })
        return render(request, "selecplan.html", context={'planes': resultados})
    elif request.method == "POST":
         plan_pk = request.POST['plan']
         usuario = Usuario.objects.get(email=request.user.email)


         if plan_pk:
            plan = Plan.objects.get(id=plan_pk)
            nueva_suscripcion = Suscripcion.objects.create(
                SusActiva=True,
                usuario=usuario,
                nombre_plan=plan,
            )
            nueva_suscripcion.save()
            return redirect('/frontpage')


def crear_suscripcion(request):
    if request.method == "POST":
        plan_pk = request.POST.get('plan_pk')
        usuario = Usuario.objects.get(email=request.user.email)

        if plan_pk:
            plan = Plan.objects.get(id=plan_pk)
            nueva_suscripcion = Suscripcion.objects.create(
                SusActiva=True,
                usuario=usuario,
                nombre_plan=plan,
            )
            nueva_suscripcion.save()
            return redirect('/frontpage')
    # Manejar casos donde no se hace la solicitud POST correctamente
    return redirect('/error')






def displaypage(request):
    return render(request, "displaypage.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Ese nombre de usuario ya existe. Elija otro.")
            return redirect('/register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "La dirección de correo electrónico ya existe. Elija otra.")
            return redirect('/register')

        if pass1 != pass2:
            messages.error(request, "Las contraseñas ingresadas no coinciden. Ingreselas nuevamente.")
            return redirect('/register')

        if not username.isalnum():
            messages.error(request, "El nombre de usuario no puede contener caracteres especiales.")
            return redirect('/register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()

        myusuario = Usuario(email = email, nombre = fname, apellido=lname, password = pass1)

        myusuario.save()
        login(request, myusuario)


        messages.success(request, "Su cuenta fue creada con éxito.")
    return render(request, 'register.html')




def iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            Usuario = form.get_user()
            login(request, Usuario)
            # Redirige a la página deseada después del inicio de sesión
            return redirect('frontpage.html')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def login_fail(request):
    return render(request,"login_fail.html")

