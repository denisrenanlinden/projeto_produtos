from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'produtos/index.html')


def produtos(request):
    dados_index = {
        'frase': 'Frase para testar lá no Frontend',
        'nome': 'Lucas',
        'idade': 25,
    }
    return render(request, 'produtos/produtos.html', dados_index)
