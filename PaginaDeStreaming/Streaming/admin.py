from .models import *
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)  # Cambié 'Nombre' a 'nombre'

admin.site.register(Usuario, ClientAdmin)
admin.site.register(Plan)
admin.site.register(Tarjeta)
admin.site.register(Suscripcion)
admin.site.register(TipoTarjeta)
admin.site.register(TipoPlan)
admin.site.register(Caracteristicas)
admin.site.register(CaracteristicasXPlan)

