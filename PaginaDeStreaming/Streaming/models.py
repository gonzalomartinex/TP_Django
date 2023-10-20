from django.db import models
 

# Create your models here.
class TipoTarjeta(models.Model):
    id_tipotarjeta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

class TipoPlan(models.Model):
    idtipoplan = models.AutoField(primary_key=True)
    tipo_plan = models.CharField(max_length=50)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=50)
    numero_telefono = models.IntegerField()
    contraseña = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    def __str__(self):
        return f'{self.Nombre}, {self.Email}'
    
class Caracteristicas(models.Model):
    id_Caracteristicas = models.AutoField(primary_key=True)
    caracteristicas = models.CharField(max_length=50)
    
class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=255)
    idtipoplan = models.ForeignKey(TipoPlan, on_delete=models.CASCADE)


class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    nombreTitular = models.CharField(max_length=255)
    apellidoTitular = models.CharField(max_length=255)
    numero_tarjeta = models.BigIntegerField()
    fecha_vencimiento = models.DateField()
    codigo_seguridad = models.IntegerField()
    NumAutorizacionTarjeta = models.IntegerField()
    TipoTarjeta = models.ForeignKey(TipoTarjeta, on_delete=models.CASCADE)
    


class Suscripcion(models.Model):
    id_suscripcion = models.AutoField(primary_key=True)
    fechasuscripcion = models.DateField()
    SusActiva = models.BooleanField()
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class UsuarioxSuscripcion(models.Model):
    id_Usuarioxsuscripcion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=255)

class Planxcaracteristicas(models.Model): 
    id_Planxcaracteristicas = models.AutoField(primary_key=True)
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    id_Caracteristicas = models.ForeignKey(Caracteristicas, on_delete=models.CASCADE)
    Activa = models.BooleanField()
    detalle = models.CharField(max_length=100)