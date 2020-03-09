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
from clientes.models import Clientes
from imoveis.models import Imoveis
#from . import models
#import calendar
#import itertools
# Create your views here.

def alugados (request):

    n = n = Alugados.objects.all().count()
    lista = Alugados.objects.all()
    
    context = {
        'n': n,
        'lista' : lista,
    }

    return render(request, 'alugados/alugados.html', context)

def adicionar (request):
    
    form = AlugadosForm(request.POST)    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluguel Adicionado')
            return redirect('alugados')

    context = {
        'form': form
    }

    return render(request, 'alugados/adicionar.html', context)


def delete(request, pk):

    q = get_object_or_404(Alugados, pk=pk)
    q.delete()

    messages.warning(request, 'Aluguel Apagado!')
    return redirect('alugados')
