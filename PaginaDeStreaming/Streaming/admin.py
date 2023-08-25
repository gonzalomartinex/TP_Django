from .models import Client, Plan
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('Nombre',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Plan)
