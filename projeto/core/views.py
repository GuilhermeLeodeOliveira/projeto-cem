from django.shortcuts import render, redirect
from .models import Usuario, ProgramaPosGraduacao
from django.http import HttpResponse

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {"usuarios": usuarios}) #Retorna uma variavel com todos os dados do banco


def salvar(request):
    
    userNome = request.POST.get('nome')
    Usuario.objects.create(nome=userNome)
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})

def editar(request, id):
    
    usuario = Usuario.objects.get(id_usuario=id)
    return render(request, 'update.html', {'usuario': usuario})

def update(request, id):
    
    userNome = request.POST.get('nome')
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.nome = userNome
    usuario.save()
    return redirect(home)

def delete(request, id):
    
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect(home)

def cadastro(request):
    return render(request, 'cadastro.html')

def form_perfil(request):
    
    return render(request, 'form_perfil.html')

def selecionar_tela(request):
    opcao = request.POST.get('opcao')
    if opcao == "opcao1":
        programas = ProgramaPosGraduacao.objects.all()
        return render(request, 'cad_docente.html', {'programas': programas})
    elif opcao == "opcao2":
        return render(request, 'cadPosDout.html')
    elif opcao == "opcao3":
        return render(request, 'cadPosGrad.html')
    elif opcao == "opcao4":
        return render(request, 'cadExtern.html')
    
def cad_docente(request):
    return render(request, 'cad_docente.html')

def form_infra(request):
    return render(request, 'form_infra.html')

def form_termo(request):
    return render(request, 'form_termo.html')

def cadastrar_docente(request):
    return render(request, 'index.html')
    