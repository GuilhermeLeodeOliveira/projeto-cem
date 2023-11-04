from django.shortcuts import render, redirect
from .models import Equipamento
from administracao.models import Tecnico
from django.http import HttpResponse

def cad_equipamento(request):
    
    if 'chave' in request.session:
        user_authenticated = True
        tecnicos = Tecnico.objects.all()
        return render(request, 'cad_equipamento.html', {'user_authenticated': user_authenticated, 'tecnicos': tecnicos})
    else:
        user_authenticated = False
        return HttpResponse('Precisa estar logado para acessar essa função')


def equipamentos(request):
    return render(request, 'equipamentos.html')

def cadastrar_equipamento(request):
    novo_equipamento = Equipamento()
    novo_equipamento.nome = request.POST.get('nome')
    novo_equipamento.apelido = request.POST.get('apelido')
    novo_equipamento.descricao = request.POST.get('descricao')
    novo_equipamento.fabricante = request.POST.get('fabricante')
    novo_equipamento.localizacao = request.POST.get('localizacao')
    novo_equipamento.origem = request.POST.get('origem')
    novo_equipamento.ano_aquisicao = request.POST.get('ano_aquisicao')
    novo_equipamento.sala = request.POST.get('sala')
    novo_equipamento.divisao = request.POST.get('divisao')
    novo_equipamento.status = request.POST.get('status')
    novo_equipamento.comentario = request.POST.get('comentario')
    novo_equipamento.chave = request.POST.get('chave')
    novo_equipamento.patrimonio = request.POST.get('patrimonio')
    novo_equipamento.aquisicao = request.POST.get('aquisicao')
    novo_equipamento.prof = request.POST.get('prof')
  
    tecnico = request.POST.get('tecnico')
    tecnico_cadastrado = Tecnico.objects.get(nome=tecnico)
    novo_equipamento.id_tecnico = tecnico_cadastrado

    novo_equipamento.save()
    
    #Equipamento.objects.create(prof=prof)

    equipamento = equipamentos(request)
    return HttpResponse("Cadastrado")

