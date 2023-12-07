from django.shortcuts import render, redirect
from .models import Adm, Tecnico
from django.http import HttpResponse
from core.models import Login
from django.urls import reverse

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

            return redirect('dashboard')
        else:
            return HttpResponse('email ou senha incorretos')
        
    elif Tecnico.objects.filter(email=email).exists():
        
        tecnico = Tecnico.objects.get(email=email)
        
        if tecnico.email == email and tecnico.senha == senha:
            request.session['chave'] = tecnico.id_tecnico
            
            return redirect('perfil_tecnico')
        else:
            return HttpResponse('Email ou senha incorretos')
        
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
    user = Tecnico.objects.get(id_login=chave)
    return render(request, 'perfil_tecnico.html', {'user_authenticated': user_authenticated, 'user': user})

def encerrar_sessao_adm(request):
    request.session.flush()
    url = reverse('index.html')
                        # Redirecione para a URL obtida
    return redirect(url)

from core.models import Login
import csv
from django.contrib.auth.hashers import make_password

with open('arquivo.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # Pule a linha de cabeçalho se houver uma

    for linha in leitor_csv:
        email = linha[0]
        senha = linha[1]

        # Verifique se o usuário já existe pelo e-mail
        if not Login.objects.filter(email_inst=email).exists():
            # Criar um objeto Login com os valores padrão
            # Use make_password para armazenar a senha de forma segura
            login_objeto = Login(email_inst=email, senha=make_password(senha))

            # Salvar o objeto no banco de dados
            login_objeto.save()