# churras/views.py
from django.shortcuts import render

def index(request):
    dados = {'lista_pratos':
        {
            '1':'Picanha',
            '2':'Abobora',
            '3':'Cupim',
            '4':'Costela'
        }
    }
    return render(request, 'index.html', dados) # Renderiza o novo index.html

def churrasco(request):
    context = {'email': 'canesgril@teste.com'}
    return render(request, 'churrasco.html', context)