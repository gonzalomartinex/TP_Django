from django.shortcuts import render
from .models import *
from .forms import UsuarioRegister
from .forms import UsuarioLogin
from .forms import TarjetaForm
from .forms import PlanForm
#from .forms import PlanForm

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
            response.set_cookie('log',True)

    return response

def login(request):
    Usuario.objects
    u = Usuario.objects.all()
    logged = False

    raw_input = []
    form = UsuarioLogin
    if request.method == 'GET':
        render(request, "login.html")
    

    if request.method == 'POST':
        
        form = UsuarioLogin(request.POST)
        if form.is_valid():
            form = UsuarioLogin(request.POST)
            raw_input = request.POST
    
    str_input = raw_input.__str__()
    print('raw_input : ' + str_input)

    for x in u:
        print('u: '+x.__str__())
        print(x.email)
        print(x.contraseña)

        if str_input.find(x.email) == -1:
            print("not this one")
        else:
            if str_input.find(x.contraseña) == -1:
                print("not this one")
            else:
                logged = True
        


    context = {'form': form}
    response = render(request, "login.html", context)
    
    if logged == True:
        response.set_cookie('log',True)
    else:
        response.set_cookie('log',False)

    return response

def login_fail(request):
    
    return render(request,"login_fail.html")

def tarjeta(request):
    form = TarjetaForm
    form2= PlanForm
    if request.method == 'POST':
        
        form = TarjetaForm(request.POST)
        if form.is_valid():
            form.save()

        form2= PlanForm(request.POST)

        if form2.is_valid():
            print(form2)
            form2.save()

    context = {
        'form': form,
        'form2' : form2
        }
    response = render(request, "tarjeta.html", context)

    if request.method == 'POST':    
        if form.is_valid():
            response.set_cookie('tarj',form.data)

    return response

def plan(request):

    

    context = {}
    response = render(request, "plan.html", context)
    return response