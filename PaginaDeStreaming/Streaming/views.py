from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import UsuarioRegister
from .forms import UsuarioLogin
from .forms import TarjetaForm
from .forms import PlanForm
import datetime
#from .forms import PlanForm

def frontpage(request):
    return render(request, "frontpage.html")

# Create your views here.


def displaypage(request):
    return render(request, "displaypage.html")

def register(request):
    
    formU = UsuarioRegister
    formT = TarjetaForm
    formP= PlanForm

    if request.method == 'GET':
        render(request, "register.html")
    

    if request.method == 'POST':
        
        formU = UsuarioRegister(request.POST)
        if formU.is_valid():
            print(formU.data)
            formU.save()
        
        formT = TarjetaForm(request.POST)
        if formT.is_valid():
            formT.save()

        formP= PlanForm(request.POST)
        if formP.is_valid():
            print(formP)
            formP.save()

    context = {
        'formU': formU,
        'formT' : formT,
        'formP' : formP
        }
    response = render(request, "register.html", context)
    
    if request.method == 'POST':    
        if formU.is_valid() and formP.is_valid() and formT.is_valid():
            response.set_cookie('log',True)

            response.set_cookie('tarj',formT.data)
            suscripcion = Suscripcion(
                fecha_suscripcion = datetime.date.today(),
                SusActiva = True,
                id_tarjeta = formT.instance,
                id_plan = formP.instance,
                id_usuario = formU.instance,
            )
            suscripcion.save()
            
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
