import csv
from django.template import loader, Context

from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Agendamento
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from equipamentos.models import Equipamento
from core.models import Docente, AlunoPosIC, UserExterno, Login
from administracao.models import Tecnico, preCadTecnico
from datetime import datetime
from treinamento.models import Solicitacoes, Treinamento
from equipamentos.models import Equipamento
# Create your views here.
def agendamentos(request):
    if 'chave' in request.session:
        # Obtenha o ID do usuário atualmente logado
        chave = request.session.get('chave')
        login = Login.objects.get(id_login=chave)
        
        # Verifique o tipo de perfil e obtenha as solicitações correspondentes
        if login.perfil == 'docente':
            user = Docente.objects.get(id_login=chave)
            solicitacoes_usuario = Solicitacoes.objects.filter(id_login=login)
            
        elif login.perfil == 'aluno' or login.perfil == 'aluno ou pos doc':
            user = AlunoPosIC.objects.get(id_login=chave)
            solicitacoes_usuario = Solicitacoes.objects.filter(id_login=login)

        elif login.perfil == 'user_externo':
            solicitacoes_usuario = Solicitacoes.objects.filter(id_UserExterno=chave)

        else:
            solicitacoes_usuario = None

        
        equipamentos = Equipamento.objects.all()
        return render(request, 'agendamento.html', {'equipamentos': equipamentos})
    else:
        return HttpResponse('Precisa estar logado para acessar essa função')
    
def calendario_equipamento(request, id_equipamento):
    agendamentos = Agendamento.objects.all()
    equipamento = get_object_or_404(Equipamento, id_equipamento=id_equipamento)
    return render(request, 'agendamentos/calendario_equipamento.html', {'equipamento': equipamento, 'agendamentos': agendamentos})
