from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class TipoTarjeta(models.Model):
    tipo_tarjeta = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.tipo_tarjeta}'


class Usuario(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=250, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    estado = models.BooleanField(default=False)
    tarjeta_id = models.ForeignKey('Tarjeta', on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'fecha_inicio']

    def __str__(self):
        return f'{self.nombre}'
    

class Telefono(models.Model):
    telefono = models.IntegerField()
    descripcion = models.TextField(max_length=250)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.telefono}'
    
class Caracteristicas(models.Model):
    caracteristica = models.CharField(max_length=50)
    detalle = models.TextField(max_length=250)
    def __str__(self):
        return f'{self.caracteristica}'


class Plan(models.Model):
    nombre_plan = models.CharField(max_length=100)
    detalle = models.TextField(max_length=255)
    
    def __str__(self):
        return f'{self.nombre_plan}'

class CaracteristicasXPlan(models.Model):
    esta_activo = models.BooleanField()
    cantidad = models.IntegerField()
    caracteristica = models.ForeignKey('Caracteristicas' ,on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan ,on_delete=models.CASCADE)
    def __str__(self):
        return f'Plan: {self.plan}, Caracteristica: {self.caracteristica}, Estado: {self.esta_activo}, Cantidad: {self.cantidad}'


class Tarjeta(models.Model):
    nombreTitular = models.CharField(max_length=255)
    apellidoTitular = models.CharField(max_length=255)
    numero_tarjeta = models.BigIntegerField(unique=True, primary_key=True)
    fecha_vencimiento = models.DateField()
    codigo_seguridad = models.IntegerField()
    TipoTarjeta = models.ForeignKey(TipoTarjeta, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.numero_tarjeta}'


class Suscripcion(models.Model):
    fecha_suscripcion = models.DateField(default=timezone.now)
    SusActiva = models.BooleanField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    def __str__(self):
        return f'Suscripción de {self.usuario.email} - Plan: {self.nombre_plan}'