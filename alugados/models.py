from django.db import models
from clientes.models import *
from imoveis.models import *

class Alugados(models.Model):

    cliente = models.ForeignKey(Clientes, related_name='cliente_alugados', on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imoveis, related_name='cliente_alugados', on_delete=models.CASCADE)
    
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.cliente}'+' '+f'{self.imovel}'