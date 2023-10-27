from django.shortcuts import render, redirect
from .models import Equipamento
from django.http import HttpResponse

def cad_equipamento(request):
    if 'chave' in request.session:
        user_authenticated = True
    else:
        user_authenticated = False

    context = {'user_authenticated': user_authenticated}
    return render(request, 'cad_equipamento.html', context)

def equipamentos(request):
    return render(request, 'equipamentos.html')

def cadastrar_equipamento(request):
    novo_equipamento = Equipamento()
    novo_equipamento.nome = request.POST.get('nome')
    novo_equipamento.apelido= request.POST.get('apelido')
    novo_equipamento.fabricante= request.POST.get('fabricante')
    novo_equipamento.localizacao= request.POST.get('localizacao')
    novo_equipamento.origem= request.POST.get('origem')
    novo_equipamento.ano_aquisicao= request.POST.get('ano_aquisicao')
    novo_equipamento.contato= request.POST.get('contato')
    novo_equipamento.sala= request.POST.get('sala')
    novo_equipamento.tipo= request.POST.get('tipo')
    novo_equipamento.status= request.POST.get('status')
    novo_equipamento.manutencao= request.POST.get('manutencao')
    novo_equipamento.comentario= request.POST.get('comentario')
    novo_equipamento.descricao= request.POST.get('descricao')
    novo_equipamento.coordenacao= request.POST.get('coordenacao')
    novo_equipamento.prof= request.POST.get('prof')
    novo_equipamento.tecnico= request.POST.get('tecnico')
    novo_equipamento.save()
    
    #Equipamento.objects.create(prof=prof)

    equipamento = equipamentos(request)
    return HttpResponse("Cadastrado")

