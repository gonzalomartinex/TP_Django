from django.shortcuts import render
from .models import *
from .forms import UsuarioRegister
from .forms import UsuarioLogin

def frontpage(request):
    return render(request, "frontpage.html")

# Create your views here.


def displaypage(request):
    return render(request, "displaypage.html")

def register(request):
    
    form = UsuarioRegister
    if request.method == 'GET':
        render(request, "register.html")
    

    if request.method == 'POST':
        
        form = UsuarioRegister(request.POST)
        if form.is_valid():
            form.save()
            #redirect('home')

    context = {'form': form}
    response = render(request, "register.html", context)
    
    if request.method == 'POST':    
        if form.is_valid():
            response.set_cookie('test',True)

    return response

def login(request):
    Usuario.objects
    u = Usuario.objects.filter(email="pepe@gmail.com")
    print(u)

    raw_input = []
    form = UsuarioLogin
    if request.method == 'GET':
        render(request, "register.html")
    

    if request.method == 'POST':
        
        form = UsuarioLogin(request.POST)
        if form.is_valid():
            form = UsuarioLogin(request.POST)
            raw_input = request.POST
    
    print(raw_input)

    for i in raw_input.copy():
        pass
        ### ME FALTA TERMINAR POR ACA

    for x in u:
        print('u: '+x.__str__())

    context = {'form': form}
    response = render(request, "register.html", context)
    

    return response

def login_fail(request):
    
    return render(request,"login_fail.html")