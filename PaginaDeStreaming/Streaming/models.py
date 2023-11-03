from django.db import models
 

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=255)
    numero_telefono = models.IntegerField()
    contraseña = models.CharField()
    def __str__(self):
        return f'{self.Nombre}, {self.Email}'

class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    hd = models.BooleanField()
    ultrahd = models.BooleanField()
    pantallas = models.IntegerField()
    peliculas_y_programas_ilimitados = models.BooleanField()

class TipoPlan(models.Model):
    id_tipo_plan = models.AutoField(primary_key=True)

class Suscripcion(models.Model):
    id_suscripcion = models.AutoField(primary_key=True)
    fecha_de_suscripcion = models.DateField()

class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    numero_tarjeta = models.BigIntegerField()
    fecha_vencimiento = models.DateField()
    codigo_seguridad = models.IntegerField()

class TipoTarjeta(models.Model):
    id_tipo_tarjeta = models.AutoField(primary_key=True)
    mastercard = models.CharField(max_length=255)
    american_express = models.CharField(max_length=255)
    diners = models.CharField(max_length=255)