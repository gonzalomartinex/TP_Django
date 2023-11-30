from django.urls import path, include
from . import views
from Streaming.views import frontpage, displaypage, register, login, login_fail, selecplan


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('displaypage/', displaypage, name="displaypage"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('frontpage/', frontpage, name="frontpage"),
    path('login_fail/', login_fail, name="login_fail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('selecplan/', selecplan, name="selecplan"),
    path('crear_suscripcion/', views.crear_suscripcion, name='crear_suscripcion')
]



