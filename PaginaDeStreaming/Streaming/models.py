from django.db import models

# Create your models here.
class Client(models.Model):
    Nombre = models.CharField(max_length=50, null=True, blank=True)
    Telefono = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=50, null=True)
    Contraseña = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return f'{self.Nombre}, {self.Email}'

class Plan(models.Model):
    Precio = models.FloatField(max_length=50, null=True, blank=True)
    HD = models.BooleanField(null=True, default=True)
    UHD = models.BooleanField(default=False, null=True)
    Programas = models.BooleanField(default=True, null=True)
    Cancelar = models.BooleanField(default=True, null=True)