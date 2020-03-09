from django.db import models

class Imoveis(models.Model):

    cidade = models.CharField('Cidade', max_length=30, null=True, blank=True)
    rua = models.CharField(max_length=30, null=True, blank=True)
    numero = models.IntegerField('Número do imóvel', null=True, blank=True)
    status = models.BooleanField('Disponível', default=True)

    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.cidade}'+' - '+f'{self.rua}'