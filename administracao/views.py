from django.shortcuts import render, redirect
from .models import Adm
from django.http import HttpResponse
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

            if 'chave' in request.session:
                user_authenticated = True
            else:
                user_authenticated = False

            context = {'user_authenticated': user_authenticated}

            return render(request, 'dashboard.html', context)
    
def dashboard(request):
    return render(request, 'dashboard.html')