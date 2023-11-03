from django.shortcuts import render
from .models import *
from .forms import UsuarioForm

def frontpage(request):
    return render(request, "frontpage.html")

# Create your views here.


def displaypage(request):
    return render(request, "displaypage.html")

def register(request):

    form = UsuarioForm

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            #redirect('home')

    context = {'form': form}
    return render(request, "register.html", context)

