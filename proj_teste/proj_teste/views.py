from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse("O ano enviado foi: " + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Hugo', 'idade': 29}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    return {'nome': 'Não Encontrado', 'idade': 0}

def fname(request, nome):
    retorno = lerDoBanco(nome)
    return HttpResponse(retorno['nome'] + ' ' + str(retorno['idade']))

def fname2(request, nome):
    idade= str(lerDoBanco(nome)['idade'])
    return render(request, 'pessoa.html', {'v_idade': idade})





