
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    
    idade = 15 
    tipo = ''
    
    if idade < 18:
        tipo = 'Menor de idade'
    elif idade >= 12 and idade <= 18:
        tipo = 'Adolescente'
    else:
        tipo = 'Adulto'
            
    context = {
        'nome': 'Django básico',
        'idade': 15,
        'tipo': tipo,
        'ultimo_acesso': '10/10/2030',
        'produtos': [  # Usei minúsculo para facilitar
            {'nome': 'Notebook Acer', 'preco': 'R$ 2.500,00'},
            {'nome': 'Iphone', 'preco': 'R$ 5.000,00'},
            {'nome': 'Samsung Galaxy', 'preco': 'R$ 3.000,00'},
        ]
    }
    return render(request, 'index.html', context)

def celulares(request):
    return render(request,'celulares.html')

