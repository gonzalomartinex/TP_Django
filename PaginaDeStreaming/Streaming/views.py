from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import login
from .forms import CustomAuthenticationForm
from .forms import UsuarioRegister


def frontpage(request):
    return render(request, "frontpage.html")

# Create your views here.


def displaypage(request):
    return render(request, "displaypage.html")

def register(request):
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
            email = formU['email'].value()
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if User.objects.filter(username=username):
                print("Ese nombre de usuario ya existe. Elija otro.")
                return redirect('/register')

            if User.objects.filter(email=email).exists():
                print("La dirección de correo electrónico ya existe. Elija otra.")
                return redirect('/register')

            if pass1 != pass2:
                print("Las contraseñas ingresadas no coinciden. Ingreselas nuevamente.")
                return redirect('/register')

            if not username.isalnum():
                print("El nombre de usuario no puede contener caracteres especiales.")
                return redirect('/register')
            
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.is_active = True
            myuser.save()

            myusuario = Usuario(email = email, nombre = fname, apellido=lname, password = pass1)
            myusuario.save()

            messages.success(request, "Su cuenta fue creada con éxito.")
    return response




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
