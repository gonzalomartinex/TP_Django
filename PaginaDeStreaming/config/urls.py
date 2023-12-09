"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from Streaming.views import frontpage, displaypage, registerView, login_failView, loginView, planView, tarjetaView, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name="frontpage"),
    path('frontpage/', frontpage, name="frontpage"),
    path('displaypage/', displaypage, name="displaypage"),
    path('register/', registerView, name="register"),
    path('login/', loginView, name="login"),
    path('login_fail/', login_failView, name="login_fail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('plan/', planView, name="plan"),
    path('tarjeta/', tarjetaView, name="tarjeta"),
    path('logout/', logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls'))
]