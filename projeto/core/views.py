from django.shortcuts import render
from .models import Usuario

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {"usuarios": usuarios}) #Retorna uma variavel com todas os dados do banco


def salvar(request):
    
    userNome = request.POST.get('nome')
    Usuario.objects.create(nome=userNome)
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})