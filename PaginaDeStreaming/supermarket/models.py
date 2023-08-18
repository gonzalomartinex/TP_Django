from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    cuit = models.CharField(max_length=15, null=True)
    created_at = models.CharField(max_length=50)
    socio = models.CharField(max_length=50, default=True)
    socio_number = models.CharField(max_length=50)

def __str__(self):
    return f'{self.name}, {self.last_name}'