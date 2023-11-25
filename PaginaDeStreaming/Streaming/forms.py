from django.forms import ModelForm
from .models import Usuario

class UsuarioRegister(ModelForm):
    class Meta:
        model = Usuario
        fields= '__all__'

class UsuarioLogin(ModelForm):
    class Meta:
        model = Usuario
        fields= ["nombre","contraseña"]