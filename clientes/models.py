from django.db import models

class Clientes(models.Model):

    nome = models.CharField('Nome', max_length=30, null=True, blank=True)
    sobrenome = models.CharField(max_length=30, null=True, blank=True)
    data_nasc = models.DateField('Data de Nascimento', blank=True, null=True)
    cpf = models.CharField('CPF', max_length=30)
    status = models.BooleanField('Ativo', default=True)

    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome