from django.shortcuts import render, redirect
#from .models import 
from django.http import HttpResponse

# Create your views here.

def treinamento(request):
    if 'chave' in request.session:
        user_authenticated = True
        context = {'user_authenticated': user_authenticated}
        return render(request, 'treinamento.html', context)
    else:
        user_authenticated = False
        return HttpResponse('Precisa estar logado para acessar essa função')
    