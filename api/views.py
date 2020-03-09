from django.shortcuts import render
from clientes.models import Clientes
from imoveis.models import Imoveis
from alugados.models import Alugados
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

class lista_clientes (APIView):

    def get(self, request):
       
        lista_clientes = Clientes.objects.all().order_by('nome')

        lista = []
         
        for x in lista_clientes:
            c = {}
            c['id'] = x.pk
            c['nome'] = x.nome
            c['sobrenome'] = x.sobrenome
            c['data_nasc'] = x.data_nasc
            c['cpf'] = x.cpf
            c['status'] = x.status
            lista.append(c)


        return Response({'Lista': lista})

class lista_imoveis (APIView):

    def get(self, request):
       
        lista_imoveis = Imoveis.objects.all().order_by('cidade')

        lista = []
         
        for x in lista_imoveis:
            c = {}
            c['id'] = x.pk
            c['cidade'] = x.cidade
            c['rua'] = x.rua
            c['numero'] = x.numero
            c['status'] = x.status
            lista.append(c)


        return Response({'Lista': lista})

class lista_alugueis (APIView):

    def get(self, request):
              
        lista_alugueis = Alugados.objects.all()

        lista = []

        for x in lista_alugueis:
            c = {}
            c['pk'] = x.pk

            clientes = Clientes.objects.filter(pk=x.fk_cliente)
            for y in clientes:
                c['nome'] = str(y.nome)+' '+str(y.sobrenome)
            
            imoveis = Imoveis.objects.filter(pk=x.fk_imovel)
            for z in imoveis:
                c['endereco'] = str(z.cidade)+', '+str(z.rua)+', '+str(z.numero)
            lista.append(c)


        return Response({'Lista': lista})