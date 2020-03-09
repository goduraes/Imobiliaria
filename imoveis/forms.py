#Esta importaçao é da biblioteca de formularios do django
from django import forms

#É a importação do model que quer criar o formulário
from .models import Imoveis

class ImoveisForm(forms.ModelForm):

    class Meta:
        model = Imoveis
        #fields = ('nome', 'sobrenome',)
        fields = '__all__' 
        #-> imprime todos os campos
        #exclude=('nome') -> todos menos nome