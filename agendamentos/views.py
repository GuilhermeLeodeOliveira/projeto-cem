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
    contexto={}
    if 'perfil' in request.session and request.session['perfil'] == 'aluno ou pos doc' or request.session['perfil'] == 'tecnico' or request.session['perfil'] == 'docente':
    
        login = Login.objects.get(id_login=chave)
        
        if request.session['perfil'] == 'aluno ou pos doc':
            nome = AlunoPosIC.objects.get(id_login=login).primeiro_nome
            orientador = AlunoPosIC.objects.get(id_login=login).nome_orientador

        elif request.session['perfil'] == 'docente':
            nome = Docente.objects.get(id_login=login).primeiro_nome
            orientador = Docente.objects.get(id_login=login).primeiro_nome
        
        elif request.session['perfil'] == 'tecnico':
            nome = Tecnico.objects.get(id_login=login).primeiro_nome
            orientador = Tecnico.objects.get(id_login=login).primeiro_nome

        contexto.update({
            'nome': nome,
            'orientador': orientador,
        })
    
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
    agendamento_existente = Agendamento.objects.filter(id_equipamento=equipamento).exclude(status="cancelado")
    
    value = datetime.now().date()
    
    # Passe os dados relevantes para o template
    contexto.update({
        'equipamento': equipamento,
        'meses': meses,
        'data_atual': data_atual,
        'horarios': horarios,
        'lista_dias_anteriores': lista_dias_anteriores,
        'value': value,
        'agendamento_existente': agendamento_existente,
        'login': login,
    })


    return render(request, 'agendamentos/calendario_equipamento.html', contexto)    


def realizar_agendamento(request):

    id_equipamento = request.session.get('id_equipamento')
    id_login = request.session.get('chave')

    equipamento = Equipamento.objects.get(id_equipamento=id_equipamento)
    login = Login.objects.get(id_login=id_login)

    data = request.POST.get('data')
    horaInicio = request.POST.get('horarioInicio')
    horarioTermino = request.POST.get('horarioTermino')
    nome = request.POST.get('nome')
    orientador = request.POST.get('orientador')
    informacao_adicional = request.POST.get('informacao_adicional')
    
    # Verifica se já existe um agendamento para a data e horário fornecidos
    agendamento_existente = Agendamento.objects.filter(
        data_agendada=data,
        hora_inicio_agendamento=horaInicio,
        status="pendente"
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
        status = "pendente",
        nome_orientador=orientador,
        nome_usuario=nome,
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

def verifica_perfil(request, email):
    if request.session.get('perfil') == "tecnico":  # Verifica se a chave 'perfil' existe na sessão
        # Faça o que precisa com o email aqui
        return dados_user(request, email)
    else:
        return HttpResponse("nada")

def dados_user(request, email):
    try:
        # Tente buscar o usuário pelo email na tabela de Login
        login = Login.objects.get(email_inst=email)
        
        # Verifique se existe um aluno com este login
        aluno = AlunoPosIC.objects.filter(id_login=login).first()
        if aluno:
            return render(request, 'administracao/dados_user.html', {'aluno': aluno, 'login':login})
        
        # Verifique se existe um docente com este login
        docente = Docente.objects.filter(id_login=login).first()
        if docente:
            return render(request, 'administracao/dados_user.html', {'docente': docente, 'login':login})
        
        # Se não foi encontrado nem aluno nem docente, retorne uma mensagem de usuário não encontrado
        return HttpResponse('Usuário não encontrado')
        
    except Login.DoesNotExist:
        # Se não foi encontrado nenhum login com este email, retorne uma mensagem de usuário não encontrado
        return HttpResponse('Usuário não encontrado')
    except Exception as e:
        # Se ocorrer qualquer outro erro, retorne uma mensagem de erro genérica
        return HttpResponse(f'Ocorreu um erro: {e}')

def cancelar_agendamento(request):
    if request.method == 'GET':

        chave = request.session['chave']
        if request.session['perfil'] == 'tecnico':
        
            email = request.GET.get('email')
            data = request.GET.get('data')
            horario_inicio = request.GET.get('horarioInicio')
            horario_termino = request.GET.get('horarioTermino')
            usuario = request.GET.get('nome')
            orientador = request.GET.get('orientador')
            equipamento = request.GET.get('equipamento')
        # Faça o que for necessário com esses dados, como cancelar o agendamento
        # Por exemplo, você pode usar esses dados para encontrar e cancelar o agendamento no seu banco de dados
        
        # Realiza a consulta ao banco de dados para encontrar o agendamento
        try:
            agendamento = Agendamento.objects.get(
                data_agendada=data,
                hora_inicio_agendamento=horario_inicio,
                hora_termino_agendamento=horario_termino,
                id_login__email_inst=email,
                nome_orientador=orientador,
                nome_usuario=usuario,
                id_equipamento__nome=equipamento
            )
            
            # Agora você pode fazer o que for necessário com o agendamento, como cancelá-lo
            agendamento.status="cancelado"
            agendamento.save()  # Exemplo de como cancelar o agendamento (eliminar do banco de dados)
            
            return redirect(agendamentos)  # ou redirecione para onde for necessário
        except Agendamento.DoesNotExist:
            return HttpResponse("Agendamento não encontrado.")
        
    else:
        return HttpResponse("Método de requisição inválido.")
    