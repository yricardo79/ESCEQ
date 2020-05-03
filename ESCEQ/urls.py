"""ESCEQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from registroEquinos import views
from registroEquinos.views import saludo, despedida, registroEquino, regHistoriaClinica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_equinos/', views.busqueda_equinos),
    path('buscar/', views.bus_ser_equ),
    path('contacto/', views.Contacto),

    path('saludo/', saludo),
    path('despedida/', despedida),
    path('registroEquino/', registroEquino),
    path('regHistoriaClinica/', regHistoriaClinica),

]
