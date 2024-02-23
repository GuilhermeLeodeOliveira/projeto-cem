from django.shortcuts import render, redirect
from .models import Adm, Tecnico
from django.http import HttpResponse
from core.models import Login
from django.urls import reverse
from datetime import datetime
from agendamentos.models import Agendamento, Mes, Dia
from django.contrib.auth.hashers import check_password

# Create your views here.
def login_adm(request):
    return render(request, 'login_adm.html')

def verifica_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if Adm.objects.filter(email=email).exists():
        
        adm = Adm.objects.get(email=email)
        
        if adm.email == email and adm.senha == senha:
            request.session['chave'] = adm.id_adm
            request.session['perfil'] = 'adm'
            return redirect('dashboard')
        else:
            return HttpResponse('email ou senha incorretos')
        
    elif Login.objects.filter(email_inst=email).exists():
        
        login = Login.objects.get(email_inst=email)
        
        if login.email_inst == email and check_password(senha, login.senha):
            tecnico = Tecnico.objects.get(id_login=login)
            request.session['chave'] = tecnico.id_tecnico
            
            return redirect('perfil_tecnico')
        else:
            return HttpResponse(f'Email ou senha incorretos. Email: {email}, Senha: {senha}')
        
    else:
        return HttpResponse('Usuário não cadastrado')
    
def dashboard(request):
    
    if 'chave' in request.session:
        user_authenticated = True
    else:
        user_authenticated = False
        return HttpResponse('Você precisa estar logado para acessa a página')
    
    context = {'user_authenticated': user_authenticated}
    return render(request, 'dashboard.html', context)
            
def perfil_tecnico(request):
    
    if 'chave' in request.session:
        user_authenticated = True
    else:
        user_authenticated = False
        return HttpResponse('Você precisa estar logado para acessa a página')
    
    chave = request.session['chave']
    request.session['perfil'] = 'tecnico'
    user = Tecnico.objects.get(id_tecnico=chave)
    login = Login.objects.get(id_login=user.id_login.id_login)
    login.data_ultimo_login = datetime.now()
    login.save()

    return render(request, 'perfil_tecnico.html', {'user_authenticated': user_authenticated, 'user': user, 'login': login})

def encerrar_sessao_adm(request):
    request.session.flush()
    return render(request, 'login_adm.html')

def edita_dados_tecnico(request):
    chave = request.session['chave']
    user = Tecnico.objects.get(id_login=chave)
    login = Login.objects.get(id_login=chave)
    return render(request, 'edita_dados_tecnico.html', {'user': user, 'login': login})

def editando_dados_tecnico(request):

    chave = request.session['chave']
    
    primeiro_nome = request.POST.get('primeiro_nome')
    segundo_nome = request.POST.get('segundo_nome')
    celular = request.POST.get('tel')
    matricula_siape = request.POST.get('mat_siape')
    ramal_lab = request.POST.get('lab')

    login = Login.objects.get(id_login=chave)
    login.email_inst = request.POST.get('email_inst')
    login.save()

    tecnico = Tecnico.objects.get(id_login=chave)
    tecnico.primeiro_nome = primeiro_nome
    tecnico.segundo_nome = segundo_nome
    tecnico.celular = celular
    tecnico.matricula_siape = matricula_siape
    tecnico.ramal_lab = ramal_lab

    if request.POST.get('centro') == 'outro_centro':
        if request.POST.get('input_outro_centro'):

            tecnico.centro = request.POST.get('input_outro_centro')
        else:
            mensagem_outro_centro = 'Se você possui outro tipo de centro, precisa digitar qual é'
            return render(request, 'edita_dados_user.html', {'mensagem_outro_centro': mensagem_outro_centro})
    else:
        tecnico.centro = request.POST.get('centro')

    
    tecnico.save()

    return redirect(perfil_tecnico)

def form_calendario(request):
    if 'chave' in request.session:
        user_authenticated = True
    else:
        user_authenticated = False
        return HttpResponse('Você precisa estar logado para acessa a página')
    
    context = {'user_authenticated': user_authenticated}
    return render(request, 'form_calendario.html', context)


#def cadastrar_calendario(request):
#    if request.method == 'POST':
#        ano = request.POST.get('ano')
#        mes = request.POST.get('mes')
#        qtdDias = request.POST.get('qtdDias')
#
#        novo_calendario = Calendario()
#        novo_calendario.ano = ano
#        novo_calendario.mes = mes
#        novo_calendario.quantidade_dias = qtdDias
#        novo_calendario.save()
#
#        return HttpResponse('Cadastro concluído com sucesso.')
#
#    return render(request, 'form_calendario.html', {'form_calendario': form_calendario})