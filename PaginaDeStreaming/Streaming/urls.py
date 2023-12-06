from django.urls import path, include
from . import views
from Streaming.views import frontpage, displaypage, register, iniciar_sesion, login_fail,selecplan,logout,RegistTarjeta,contenido


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('displaypage/', displaypage, name="displaypage"),
    path('register/', register, name="register"),
    path('login/', iniciar_sesion, name="iniciar_sesion"),
    path('frontpage/', frontpage, name="frontpage"),
    path('login_fail/', login_fail, name="login_fail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('selecplan/', selecplan, name="plan"),
    path('logout/', logout, name='logout'),
    path('registtargeta/', RegistTarjeta, name='RegistTarjeta'),
    path('contenido/', contenido, name='contenido')
]



