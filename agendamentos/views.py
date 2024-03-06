import csv
from django.template import loader, Context

from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from datetime import timedelta
from core.views import perfil_user
from administracao.views import Adm, Tecnico
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
    
def mesParaNumero(mes_nome):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return str(meses.index(mes_nome.lower()) + 1).zfill(2)


def mesParaNumero(mes_nome):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return str(meses.index(mes_nome.lower()) + 1).zfill(2)

def calendario_equipamento(request, id_equipamento):
    request.session['id_equipamento'] = id_equipamento

    # Obtenha os objetos relevantes do banco de dados
    equipamento = get_object_or_404(Equipamento, id_equipamento=id_equipamento)

    # Obtenha a data e a hora atuais
    data_atual = datetime.now().date()

    chave = request.session['chave']

    if 'perfil' in request.session and request.session['perfil'] == 'aluno ou pos doc' or request.session['perfil'] == 'tecnico':
        login = Login.objects.get(id_login=chave)

    else:
        login = Adm.objects.get(id_adm=chave)
    
    # Obtenha o mês e o ano atuais
    mes_atual = data_atual.month
    ano_atual = data_atual.year
    dia_atual = data_atual.day
    
    # Filtra os meses com ano maior ou igual ao atual e nome maior ou igual ao mês atual
    meses = Mes.objects.filter(ano__gte=ano_atual, nome__gte=mes_atual)

    # Consulte o banco de dados para obter todos os dias anteriores ao dia atual
    dias_anteriores = Dia.objects.filter(mes__ano__lte=ano_atual, mes__nome__lte=mes_atual, numero__lte=data_atual.day)

    # Crie uma lista de dias anteriores
    lista_dias_anteriores = [dia.numero for dia in dias_anteriores]

    # Crie uma lista de horários
    horarios = []
    hora_inicial = 8.0  # Começando às 8:00
    while hora_inicial <= 22.0:
        hora_formatada = f'{int(hora_inicial)}:{int((hora_inicial % 1) * 60):02d}'
        horarios.append(hora_formatada.zfill(5))  # Adiciona zeros à esquerda se necessário
        hora_inicial += 0.5  # Incremento de 30 minutos
        
    # Filtra os agendamentos para o equipamento, dia e hora específicos
    agendamento_existente = Agendamento.objects.filter(id_equipamento=equipamento)
    
    value = datetime.now().date()

    # Passe os dados relevantes para o template
    contexto = {
        'equipamento': equipamento,
        'meses': meses,
        'data_atual': data_atual,
        'horarios': horarios,
        'lista_dias_anteriores': lista_dias_anteriores,
        'value': value,
        'agendamento_existente': agendamento_existente,
        'login': login,
    }


    return render(request, 'agendamentos/calendario_equipamento.html', contexto)


def realizar_agendamento(request):

    id_equipamento = request.session.get('id_equipamento')
    id_login = request.session.get('chave')

    equipamento = Equipamento.objects.get(id_equipamento=id_equipamento)
    login = Login.objects.get(id_login=id_login)

    data = request.POST.get('data')
    horaInicio = request.POST.get('horarioInicio')
    horarioTermino = request.POST.get('horarioTermino')
    informacao_adicional = request.POST.get('informacao_adicional')

    # Verifica se já existe um agendamento para a data e horário fornecidos
    agendamento_existente = Agendamento.objects.filter(
        data_agendada=data,
        hora_inicio_agendamento=horaInicio
    ).exists()

    if agendamento_existente:
        mensagem = 'Já existe um agendamento para esta data e horário. Por favor, escolha outra.'
        return HttpResponse(mensagem)

    # Se não existir agendamento, cria o novo agendamento
    novo_agendamento = Agendamento(
        data_agendada=data,
        hora_inicio_agendamento=horaInicio,
        hora_termino_agendamento=horarioTermino,
        additional_info=informacao_adicional,
        data_solicitacao_agendamento = datetime.now().date(),
        hora_solicitacao_agendamento = datetime.now().time(),
        id_equipamento = equipamento,
        id_login = login
    )
    novo_agendamento.save()

    # Restante do seu código...

    # Redireciona de volta para a view calendario_equipamento
    return redirect(agendamentos_user)
    

def agendamentos_user(request):
    if 'chave' in request.session:

        chave = request.session['chave']
        login = Login.objects.get(id_login=chave)

        if login.perfil == 'docente':
            user = Docente.objects.get(id_login=chave)
            #return render(request, 'perfil_user.html', {'docente': docente})
        
        elif login.perfil == 'aluno ou pos doc':
            
            user = AlunoPosIC.objects.get(id_login=chave)
            #return render(request, 'perfil_user.html', {'aluno_pos_ic': aluno_pos_ic})

        elif login.perfil == 'user_externo':
            user = UserExterno.objects.get(id_login=chave)
            #return render(request, 'perfil_user.html', {'user_externo': user_externo})

        agendamentos = Agendamento.objects.filter(id_login=login)


        
        return render(request, 'agendamentos_user.html', {'user': user, 'login': login, 'agendamentos': agendamentos})

