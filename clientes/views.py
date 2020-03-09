from django.shortcuts import render, redirect, get_object_or_404

from .models import *
#from django.contrib.auth.decorators import login_required
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.list import ListView
#from django.urls import reverse_lazy, reverse
from django.db.models import Count, Min, Sum, Avg
#from datetime import datetime, timedelta, date , time
#from django.utils import timezone
from .forms import *
#from django.http import HttpResponse
#from django.urls import reverse
#from django.core.mail import send_mail
#from django.core import serializers
#from django.db.models import Q
#import json
#from django.apps import apps

#Exemplo de importação de arquivos de classes e metodos externos
#from legacy.tendencias_anteriores import *

#Exemplo de importação de modelos e forms de outros apps
#sac é o nome da aplicação. é um exemplo
#from sac.models import *
#from sac.forms import AccForm, AssuntoForm, ResolucaoForm

# Create your views here.
#import csv
#from decimal import Decimal
from django.contrib import messages
#from . import models
#import calendar
#import itertools
from imoveis.models import Imoveis
from alugados.models import Alugados
# Create your views here.
def home (request):

    registros_bd = Clientes.objects.all()
    n_clientes = Clientes.objects.all().count()

    registros_imoveis = Imoveis.objects.all()
    n_imoveis = Imoveis.objects.all().count()

    registros_alugados = Alugados.objects.all()
    n_alugados = Alugados.objects.all().count()
    
    context = {
        'n_clientes': n_clientes,
        'n_imoveis': n_imoveis,
        'n_alugados': n_alugados,
    }

    return render(request, 'clientes/home.html', context)

def clientes (request):

    registros_bd = Clientes.objects.all().order_by('nome')
    n = Clientes.objects.all().count()
    
    context = {
        'n': n,
        'registros_bd' : registros_bd,
    }

    return render(request, 'clientes/clientes.html', context)

def adicionar (request):

    form = ClientesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Cliente Adicionado!')
            return redirect('clientes')

    context = {
        'form': form,
    }

    return render(request, 'clientes/adicionar.html', context)

def delete(request, pk):

    q = get_object_or_404(Clientes, pk=pk)
    q.delete()

    messages.warning(request, 'Cliente Apagado!')
    return redirect('clientes')

def edit(request, pk):
    
    q = get_object_or_404(Clientes, pk=pk)
    form = ClientesForm(request.POST or None, instance=q)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente Editado!')
            return redirect('clientes')
    
    context = {
        'form': form,
        'id': pk
    }
    return render(request, 'clientes/editar.html', context)