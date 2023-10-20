from .models import *
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('Nombre',)


admin.site.register(Usuario, ClientAdmin)
admin.site.register(Plan, TipoPlan)
admin.site.register(Tarjeta, TipoTarjeta)
admin.site.register(Suscripcion)