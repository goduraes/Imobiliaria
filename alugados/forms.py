#Esta importaçao é da biblioteca de formularios do django
from django import forms

#É a importação do model que quer criar o formulário
from .models import Alugados

class AlugadosForm(forms.ModelForm):

    class Meta:
        model = Alugados
       
        fields = '__all__' 
       