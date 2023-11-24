from django.forms import ModelForm
from .models import Usuario
from .models import Tarjeta
from .models import Plan

class UsuarioRegister(ModelForm):
    class Meta:
        model = Usuario
        fields= '__all__'

class UsuarioLogin(ModelForm):
    class Meta:
        model = Usuario
        fields= ["email","contraseña"]

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields= '__all__'

#class PlanForm(ModelForm):
#    class Meta:
#        model = Plan
#        fields = '__all__'