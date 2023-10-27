from django.shortcuts import render, redirect
from .models import Usuario, ProgramaPosGraduacao, Docente, preCadDocente, FormTermo 
from .models import FormInfra, preCadPosDout, PosDout, preCadAlunoPosIC, AlunoPosIC
from .models import preCadUserExterno, UserExterno
from django.http import HttpResponse
from PIL import Image
import os
from django.conf import settings
from django import forms
from django.core.exceptions import ObjectDoesNotExist

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
        request.session['perfil'] = "docente"
        return render(request, 'cad_docente.html', {'programas': programas})
    elif opcao == "opcao2":
        request.session['perfil'] = "pos_dout"
        return render(request, 'cad_pos_dout.html')
    elif opcao == "opcao3":
        request.session['perfil'] = "aluno_pos_dout_ic"
        return render(request, 'cad_aluno_pos_dout_ic.html')
    elif opcao == "opcao4":
        request.session['perfil'] = "user_externo"
        return render(request, 'cad_user_externo.html')
    
def cad_docente(request):
    return render(request, 'cad_docente.html')

def form_infra(request):

    perfil = request.session.get('perfil', 'valor_padrão')

    if perfil == "docente":
        novo_docente = preCadDocente()
        novo_docente.nome = request.POST.get('nome')
        novo_docente.celular = request.POST.get('tel')
        novo_docente.email_inst = request.POST.get('email_inst')
        novo_docente.senha = request.POST.get('senha')
        novo_docente.matricula_siape = request.POST.get('mat_siape')
        novo_docente.ramal_lab = request.POST.get('lab')
        novo_docente.centro = request.POST.get('centro')
        novo_docente.possui_projeto = request.POST.get('possui_projeto')
        novo_docente.programa_pos = "programa pos"
        projeto = request.POST.get('projeto')
        titulo = request.POST.get('titulo')
        vigencia = request.POST.get('vigencia')
        texto_composto = f"{projeto} - {titulo} - {vigencia}"
        novo_docente.info_projeto = texto_composto
        lista_publi = request.POST.get('publicacoes')
        novo_docente.lista_publi = lista_publi
        novo_docente.save()
        request.session['chave'] = novo_docente.id_pre_cad_docente
    
    elif perfil == "pos_dout":
        novo_aluno_pos_dout = preCadPosDout()
        
        novo_aluno_pos_dout.nome = request.POST.get('nome')
        novo_aluno_pos_dout.celular = request.POST.get('tel')
        novo_aluno_pos_dout.email_inst = request.POST.get('email_inst')
        novo_aluno_pos_dout.senha = request.POST.get('senha')
        novo_aluno_pos_dout.matricula_ufabc = request.POST.get('matricula_ufabc')
        novo_aluno_pos_dout.ramal_lab = request.POST.get('lab')
        novo_aluno_pos_dout.nome_supervisor = request.POST.get('nome_supervisor')
        novo_aluno_pos_dout.centro = "centro ufabc"
        novo_aluno_pos_dout.data_pos = request.POST.get('data_inicio')
        novo_aluno_pos_dout.possui_bolsa = request.POST.get('bolsa')
        novo_aluno_pos_dout.programa_pos = "programa pos"
        novo_aluno_pos_dout.plano_trabalho = request.POST.get('plano_trabalho')
        novo_aluno_pos_dout.declaracao_ciencia_supervisor = request.POST.get('declaracao_supervisor')
        novo_aluno_pos_dout.save()
        request.session['chave'] = novo_aluno_pos_dout.id_pre_cad_pos_dout
   
    elif perfil == "aluno_pos_dout_ic":
        novo_aluno_pos_ic = preCadAlunoPosIC()
        novo_aluno_pos_ic.nome = request.POST.get('nome')
        novo_aluno_pos_ic.celular = request.POST.get('tel')
        novo_aluno_pos_ic.email_inst = request.POST.get('email_inst')
        novo_aluno_pos_ic.senha = request.POST.get('senha')
        novo_aluno_pos_ic.matricula_ufabc = request.POST.get('matricula_ufabc')
        novo_aluno_pos_ic.ramal_lab = request.POST.get('lab')
        novo_aluno_pos_ic.nome_orientador = request.POST.get('nome_supervisor')
        novo_aluno_pos_ic.departamento = "departamento"
        novo_aluno_pos_ic.data_pos = request.POST.get('data_inicio')
        novo_aluno_pos_ic.programa_pos = "programa pos"
        novo_aluno_pos_ic.centro = request.POST.get('centro')
        novo_aluno_pos_ic.possui_bolsa = request.POST.get('bolsa')
        novo_aluno_pos_ic.plano_trabalho = request.POST.get('plano_trabalho')
        novo_aluno_pos_ic.declaracao_orientador = request.POST.get('declaracao_orientador')
        novo_aluno_pos_ic.save()
        request.session['chave'] = novo_aluno_pos_ic.id_pre_cad_aluno_pos_ic
        return render(request, 'form_infra.html')
    
    elif perfil == "user_externo":
        novo_user_externo = preCadUserExterno()
        novo_user_externo.nome = request.POST.get('nome')
        novo_user_externo.instituicao = request.POST.get('instituicao')
        novo_user_externo.atividade = request.POST.get('atividade')
        novo_user_externo.endereco_inst = request.POST.get('endereco_inst')
        novo_user_externo.celular = request.POST.get('tel')
        novo_user_externo.email_inst = request.POST.get('email_inst')
        novo_user_externo.senha = request.POST.get('senha')
        novo_user_externo.telefone_sala = request.POST.get('lab')
        novo_user_externo.formacao = request.POST.get('formacao')
        novo_user_externo.classificacao = request.POST.get('classificacao')
        novo_user_externo.nome_centro_docente = request.POST.get('nome_centro_docente')
        novo_user_externo.possui_projeto = request.POST.get('possui_projeto')
        novo_user_externo.infos_projeto = request.POST.get('infos_projeto')
        novo_user_externo.publicacoes = request.POST.get('publicacoes')
        novo_user_externo.plano_trabalho = request.POST.get('plano_trabalho')
        novo_user_externo.manifesto_apoio = request.POST.get('apoio')
        novo_user_externo.arquivo = request.FILES.get('arquivo')
        novo_user_externo.save()
        request.session['chave'] = novo_user_externo.id_pre_cad_user_externo
        
    return render(request, 'form_infra.html')

def form_termo(request):
    chave = request.session.get('chave', 'valor_padrão')
    chave_infra = request.session.get('chave_infra', 1)
    
    return render(request, 'form_termo.html')

def cadastrar_usuario(request):

    novo_termo = FormTermo()
    novo_termo.veracidade1 = request.POST.get('veracidade1')
    novo_termo.veracidade2 = request.POST.get('veracidade2')
    novo_termo.veracidade3 = request.POST.get('veracidade3')
    novo_termo.save()

    chave_termo = novo_termo.id_form_termo

    nova_infra = FormInfra()
    nova_infra.cem_sbc_equip = request.POST.get('veracidade1')
    nova_infra.cem_sbc_equip_apoio = request.POST.get('veracidade2')
    nova_infra.cem_sa_equip = request.POST.get('veracidade3')
    nova_infra.save()

    chave_infra = nova_infra.id_form_infra

    chave = request.session.get('chave', 'valor_padrão')
    
    perfil = request.session.get('perfil', 'valor_padrao')

    if perfil == "docente":

        docente = preCadDocente.objects.get(id_pre_cad_docente=chave)

        if Docente.objects.filter(email_inst=docente.email_inst).exists() or PosDout.objects.filter(email_inst=docente.email_inst).exists() or AlunoPosIC.objects.filter(email_inst=docente.email_inst).exists() or UserExterno.objects.filter(email_inst=docente.email_inst).exists():
            # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
            return HttpResponse("Esse email já possui cadastro")
            
        novo_docente = Docente()
        novo_docente.nome = docente.nome
        novo_docente.celular = docente.celular
        novo_docente.email_inst = docente.email_inst
        novo_docente.senha = docente.senha
        novo_docente.matricula_siape = docente.matricula_siape
        novo_docente.ramal_lab = docente.ramal_lab
        novo_docente.centro = docente.centro
        novo_docente.possui_projeto = docente.possui_projeto
        novo_docente.programa_pos = docente.programa_pos
        novo_docente.programa_pos = docente.programa_pos
        novo_docente.info_projeto = docente.info_projeto
        novo_docente.lista_publi = docente.lista_publi
        novo_docente.id_form_infra = nova_infra
        novo_docente.id_form_termo = novo_termo
        novo_docente.save()
    
    elif perfil == "pos_dout":
        pos_dout = preCadPosDout.objects.get(id_pre_cad_pos_dout=chave)

        if Docente.objects.filter(email_inst=pos_dout.email_inst).exists() or PosDout.objects.filter(email_inst=pos_dout.email_inst).exists() or AlunoPosIC.objects.filter(email_inst=pos_dout.email_inst).exists() or UserExterno.objects.filter(email_inst=pos_dout.email_inst).exists():
                # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
            return HttpResponse("Esse email já possui cadastro")

        novo_pos_dout = PosDout()
        novo_pos_dout.nome = pos_dout.nome
        novo_pos_dout.celular = pos_dout.celular
        novo_pos_dout.email_inst = pos_dout.email_inst
        novo_pos_dout.senha = pos_dout.senha
        novo_pos_dout.matricula_ufabc = pos_dout.matricula_ufabc
        novo_pos_dout.ramal_lab = pos_dout.ramal_lab
        novo_pos_dout.nome_supervisor = pos_dout.nome_supervisor
        novo_pos_dout.centro = pos_dout.centro
        novo_pos_dout.data_pos = pos_dout.data_pos
        novo_pos_dout.possui_bolsa = pos_dout.possui_bolsa
        novo_pos_dout.programa_pos = pos_dout.programa_pos
        novo_pos_dout.plano_trabalho = pos_dout.plano_trabalho
        novo_pos_dout.declaracao_ciencia_supervisor = pos_dout.declaracao_ciencia_supervisor
        novo_pos_dout.id_form_infra = nova_infra
        novo_pos_dout.id_form_termo = novo_termo
        novo_pos_dout.save()

    elif perfil == "aluno_pos_dout_ic":
        pos_dout_ic = preCadAlunoPosIC.objects.get(id_pre_cad_aluno_pos_ic=chave)

        if Docente.objects.filter(email_inst=pos_dout_ic.email_inst).exists() or PosDout.objects.filter(email_inst=pos_dout_ic.email_inst).exists() or AlunoPosIC.objects.filter(email_inst=pos_dout_ic.email_inst).exists() or UserExterno.objects.filter(email_inst=pos_dout_ic.email_inst).exists():
                # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
                return HttpResponse("Esse email já possui cadastro")

        novo_pos_dout_ic = AlunoPosIC()
        novo_pos_dout_ic.nome = pos_dout_ic.nome
        novo_pos_dout_ic.celular = pos_dout_ic.celular
        novo_pos_dout_ic.email_inst = pos_dout_ic.email_inst
        novo_pos_dout_ic.senha = pos_dout_ic.senha
        novo_pos_dout_ic.matricula_ufabc = pos_dout_ic.matricula_ufabc
        novo_pos_dout_ic.ramal_lab = pos_dout_ic.ramal_lab
        novo_pos_dout_ic.nome_orientador = pos_dout_ic.nome_orientador
        novo_pos_dout_ic.departamento = pos_dout_ic.departamento
        novo_pos_dout_ic.data_pos = pos_dout_ic.data_pos
        novo_pos_dout_ic.programa_pos = pos_dout_ic.programa_pos
        novo_pos_dout_ic.centro = pos_dout_ic.centro
        novo_pos_dout_ic.possui_bolsa = pos_dout_ic.possui_bolsa
        novo_pos_dout_ic.plano_trabalho = pos_dout_ic.plano_trabalho
        novo_pos_dout_ic.declaracao_orientador = pos_dout_ic.declaracao_ciencia_orientador
        novo_pos_dout_ic.id_form_termo = novo_termo
        novo_pos_dout_ic.id_form_infra = nova_infra
        novo_pos_dout_ic.save()

    elif perfil == "user_externo":
        user_externo = preCadUserExterno.objects.get(id_pre_cad_user_externo=chave)

        if Docente.objects.filter(email_inst=user_externo.email_inst).exists() or PosDout.objects.filter(email_inst=user_externo.email_inst).exists() or AlunoPosIC.objects.filter(email_inst=user_externo.email_inst).exists() or UserExterno.objects.filter(email_inst=user_externo.email_inst).exists():
                # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
                return HttpResponse("Esse email já possui cadastro")

        novo_user_externo = UserExterno()
        novo_user_externo.nome = user_externo.nome
        novo_user_externo.instituicao = user_externo.instituicao
        novo_user_externo.atividade = user_externo.atividade
        novo_user_externo.endereco_inst = user_externo.endereco_inst
        novo_user_externo.celular = user_externo.celular
        novo_user_externo.email_inst = user_externo.email_inst
        novo_user_externo.senha = user_externo.senha
        novo_user_externo.telefone_sala = user_externo.telefone_sala
        novo_user_externo.formacao = user_externo.formacao
        novo_user_externo.classificacao = user_externo.classificacao
        novo_user_externo.nome_centro_docente = user_externo.nome_centro_docente
        novo_user_externo.possui_projeto = user_externo.possui_projeto
        novo_user_externo.infos_projeto = user_externo.infos_projeto
        novo_user_externo.publicacoes = user_externo.publicacoes
        novo_user_externo.plano_trabalho = user_externo.plano_trabalho
        novo_user_externo.manifesto_apoio = user_externo.manifesto_apoio
        novo_user_externo.arquivo = user_externo.arquivo
        novo_user_externo.id_form_termo = novo_termo
        novo_user_externo.id_form_infra = nova_infra
        novo_user_externo.save()

    return redirect('login_user')

def cad_aluno_pos_dout_ic(request):
    return render(request, 'cad_aluno_pos_dout_ic.html')
    
def cad_user_externo(request):
    return render(request, 'cad_user_externo.html')

def login_user(request):
    return render(request, 'login_user.html')

def verifica_login(request):
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    
    if Docente.objects.filter(email_inst=email).exists():
        
        docente = Docente.objects.get(email_inst=email)
        
        if docente.email_inst == email and docente.senha == senha:
            request.session['chave'] = docente.id_docente
            return redirect('perfil_user')
        
    elif  PosDout.objects.filter(email_inst=email).exists():
        
        pos_dout = PosDout.objects.get(email_inst=email)

        if pos_dout.email_inst == email and pos_dout.senha == senha:
            request.session['chave'] = pos_dout.id_pos_dout
            return redirect('perfil_user')
        
    elif AlunoPosIC.objects.filter(email_inst=email).exists():
        
        aluno_pos_dou_ic = AlunoPosIC.objects.get(email_inst=email)

        if aluno_pos_dou_ic.email_inst == email and docente.senha == senha:
            request.session['chave'] = aluno_pos_dou_ic.id_aluno_pos_ic
            return redirect('perfil_user')
        
    elif UserExterno.objects.filter(email_inst=email).exists():
        
        user_externo = UserExterno.objects.get(email_inst=email)
        
        if user_externo.email_inst == email:
            request.session['chave'] = user_externo.id_user_externo
            return redirect('perfil_user')
        
    else:
        return HttpResponse('Email ou senha não encontrados')
    
        
    
def perfil_user(request):
    return render(request, 'perfil_user.html')