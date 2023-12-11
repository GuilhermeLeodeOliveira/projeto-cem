from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from administracao.models import Tecnico
from django.http import HttpResponse

def cad_equipamento(request):
    
    if 'chave' in request.session:
        user_authenticated = True
        tecnicos = Tecnico.objects.all()
        return render(request, 'cad_equipamento.html', {'user_authenticated': user_authenticated, 'tecnicos': tecnicos})
    else:
        user_authenticated = False
        return HttpResponse('Precisa estar logado para acessar essa função')

def cadastrar_equipamento(request):

    novo_equipamento = Equipamento()
    novo_equipamento.nome = request.POST.get('nome')
    novo_equipamento.apelido = request.POST.get('apelido')
    novo_equipamento.descricao = request.POST.get('descricao')
    novo_equipamento.fabricante = request.POST.get('fabricante')
    novo_equipamento.localizacao = request.POST.get('localizacao')
    novo_equipamento.origem = request.POST.get('origem')
    novo_equipamento.ano_aquisicao = request.POST.get('ano_aquisicao')
    novo_equipamento.sala = request.POST.get('sala')
    novo_equipamento.divisao = request.POST.get('divisao')
    novo_equipamento.status = request.POST.get('status')
    novo_equipamento.comentario = request.POST.get('comentario')
    novo_equipamento.chave = request.POST.get('chave')
    novo_equipamento.patrimonio = request.POST.get('patrimonio')
    novo_equipamento.aquisicao = request.POST.get('aquisicao')
    novo_equipamento.prof = request.POST.get('prof')
  
    if request.POST.get('tecnico'):
        tecnico = request.POST.get('tecnico')
        tecnico_cadastrado = Tecnico.objects.get(nome=tecnico)
        novo_equipamento.id_tecnico = tecnico_cadastrado

    novo_equipamento.save()
    
    #Equipamento.objects.create(prof=prof)

    equipamento = equipamentos(request)
    menssagem_sucesso_cadastro = 'Equipamento cadastrado com sucesso'
    return render(request, 'cad_equipamento.html', {'menssagem_sucesso_cadastro': menssagem_sucesso_cadastro})

def equipamentos(request):
    if 'chave' in request.session:
        equipamentos = Equipamento.objects.all()
        return render(request, 'tela_equipamentos.html', {'equipamentos': equipamentos})

def editar_equipamento(request, id_equipamento):
    equipamento = get_object_or_404(Equipamento, id_equipamento=id_equipamento)
    return render(request, 'equipamentos/editar_equipamento.html', {'equipamento': equipamento})

def salvar_edicao_equipamento(request, id_equipamento):
    # Obtenha o equipamento a ser editado
    equipamento = get_object_or_404(Equipamento, id_equipamento=id_equipamento)

    equipamento.nome = request.POST.get('nome')
    equipamento.apelido = request.POST.get('apelido')
    equipamento.descricao = request.POST.get('descricao')
    equipamento.fabricante = request.POST.get('fabricante')
    equipamento.localizacao = request.POST.get('localizacao')
    equipamento.origem = request.POST.get('origem')
    equipamento.ano_aquisicao = request.POST.get('ano_aquisicao')
    equipamento.sala = request.POST.get('sala')
    equipamento.divisao = request.POST.get('divisao')
    equipamento.status = request.POST.get('status')
    equipamento.comentario = request.POST.get('comentario')
    equipamento.chave = request.POST.get('chave')
    equipamento.patrimonio = request.POST.get('patrimonio')
    equipamento.aquisicao = request.POST.get('aquisicao')
    equipamento.prof = request.POST.get('prof')
    
    if request.POST.get('tecnico'):
        tecnico = request.POST.get('tecnico')
        tecnico_cadastrado = Tecnico.objects.get(nome=tecnico)
        equipamento.id_tecnico = tecnico_cadastrado

    # Salve as alterações
    equipamento.save()


    # Redirecione para a página de detalhes do equipamento ou para onde desejar
    request.session['menssagem_sucesso_edicao'] = 'Edição feita com sucesso'
    return redirect('editar_equipamento', id_equipamento=id_equipamento)