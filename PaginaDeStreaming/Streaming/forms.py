from django.forms import ModelForm
from .models import Usuario
from .models import Tarjeta
from .models import Plan
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate

class CustomAuthenticationForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label='Contraseña')

    class Meta:
        model = Usuario
        fields = ('nombre', 'password')

    def clean(self):
        nombre = self.cleaned_data.get('nombre')
        password = self.cleaned_data.get('password')

        if nombre and password:
            self.user_cache = authenticate(nombre=nombre, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Credenciales inválidas')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('Esta cuenta está inactiva')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

class UsuarioRegister(ModelForm):
    class Meta:
        model = Usuario
        fields= ["email","nombre","apellido"]

class UsuarioLogin(ModelForm):
    class Meta:
        model = Usuario
        fields= ["nombre"]

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields= '__all__'

class PlanForm(forms.Form):
    btn = forms.CharField()