import csv
from django.template import loader, Context

from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Agendamento, Dia, Mes
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
    
    data_atual = datetime.now().date()
    hora_atual = datetime.now().time()

    # Extrai o mês e o ano da data atual
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    # Filtra os objetos Calendario com base no ano e mês atual ou maiores
    meses = Mes.objects.all()

    horarios = []
    hora_inicial = 8.0  # Começando às 8:00

    while hora_inicial <= 22.0:
        horarios.append(f'{int(hora_inicial)}:{int((hora_inicial % 1) * 60):02d}')
        hora_inicial += 0.5  # Incremento de 30 minutos

    return render(request, 'agendamentos/calendario_equipamento.html', {'equipamento': equipamento, 'agendamentos': agendamentos, 'meses': meses, 'data_atual': data_atual, 'hora_atual': hora_atual, 'horarios': horarios})
