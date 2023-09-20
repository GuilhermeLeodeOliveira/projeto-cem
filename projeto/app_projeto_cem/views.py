from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'projeto/index.html')

def usuarios(request):
    #salvar os dados da tela no banco de dados
    #cadastrei usuarios no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuarios ja cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a página de listagem de usuarios
    return render(request, 'projeto/usuarios.html',usuarios)