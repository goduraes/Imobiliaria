"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from .views import *
#recomendado para importação dentro do proprio app
from clientes import views
#esse tipo de imporação faz quando vc vai importar de outro projeto

from .views import *

urlpatterns = [
    url(r'lista_clientes/', lista_clientes.as_view(), name='lista_clientes'),
    url(r'lista_imoveis/', lista_imoveis.as_view(), name='lista_imoveis'),
    url(r'lista_alugueis/', lista_alugueis.as_view(), name='lista_alugueis'),
]
