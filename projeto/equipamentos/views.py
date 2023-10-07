from django.shortcuts import render, redirect
from .models import Equipamento
from django.http import HttpResponse

def cad_equipamento(request):
    return render(request, 'cad_equipamento.html')

def equipamentos(request):
    return render(request, 'equipamentos.html')

def cadastrar_equipamento(request):
    novo_equipamento = Equipamento()
    novo_equipamento.nome = request.POST.get('nome')
    novo_equipamento.provider = request.POST.get('provider')
    novo_equipamento.tipo = request.POST.get('tipo')
    novo_equipamento.contato = request.POST.get('contato')
    novo_equipamento.status = request.POST.get('status')
    novo_equipamento.comentario = request.POST.get('comentario')
    novo_equipamento.descricao = request.POST.get('descricao')
    novo_equipamento.prof = request.POST.get('prof')
    novo_equipamento.save()
    
    #Equipamento.objects.create(prof=prof)

    equipamento = equipamentos(request)
    return HttpResponse(equipamento.content.decode())

