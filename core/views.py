from django.shortcuts import render, redirect
from .models import Usuario, ProgramaPosGraduacao, Docente, preCadDocente, FormTermo, preLogin
from .models import preCadPosDout, PosDout, preCadAlunoPosIC, AlunoPosIC, Login
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
    #elif opcao == "opcao2":
    #    request.session['perfil'] = "tecnico"
    #    return render(request, 'cad_pos_dout.html')
    elif opcao == "opcao3":
        request.session['perfil'] = "aluno_pos_dout_ic"
        return render(request, 'cad_aluno_pos_dout_ic.html')
    elif opcao == "opcao4":
        request.session['perfil'] = "user_externo"
        return render(request, 'cad_user_externo.html')
    
def cad_docente(request):
    return render(request, 'cad_docente.html')

def form_termo(request):
    perfil = request.session.get('perfil', 'valor_padrão')

    if perfil == "docente":
        verifica_email = request.POST.get('email_inst')
        if Login.objects.filter(email_inst=verifica_email).exists():
            # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
            mensagem = 'O email que você digitou já possui cadastro'
            return render(request, 'cad_docente.html', {'mensagem': mensagem})
        
        if not request.session.get('recadastro'):
            email = request.POST.get('email_inst')
            senha = request.POST.get('senha')
            novo_login = preLogin()
            novo_login.email_inst = request.POST.get('email_inst')
            novo_login.senha = request.POST.get('senha')
            novo_login.perfil = 'docente'
            novo_login.password_change_required = False
            novo_login.save()
        else:
            login = request.session.get('recadastro')
            user = Login.objects.get(id_login=login)
            user.perfil = 'docente'
            user.password_change_required = False
            user.save()

            email = user.email_inst
            senha = user.senha

            novo_login = preLogin()
            novo_login.email_inst = user.email_inst
            novo_login.senha = user.senha
            novo_login.perfil = user.perfil
            novo_login.password_change_required = user.password_change_required
            novo_login.save()
        

        novo_docente = preCadDocente()
        novo_docente.primeiro_nome = request.POST.get('primeiro_nome')
        novo_docente.segundo_nome = request.POST.get('segundo_nome')
        novo_docente.celular = request.POST.get('tel')

        novo_docente.matricula_siape = request.POST.get('mat_siape')
        novo_docente.ramal_lab = request.POST.get('lab')
        novo_docente.centro = request.POST.get('centro')

        if request.POST.get('possui_projeto') == 'sim' and request.POST.get('projeto') and request.POST.get('titulo') and request.POST.get('vigencia'):
            projeto = request.POST.get('projeto')
            titulo = request.POST.get('titulo')
            vigencia = request.POST.get('vigencia')
            texto_composto = f"{projeto} - {titulo} - {vigencia}"
            novo_docente.info_projeto = texto_composto

        elif request.POST.get('possui_projeto') == 'nao' and not request.POST.get('projeto') and not request.POST.get('titulo') and not request.POST.get('vigencia'):

            if request.POST.get('projeto') and request.POST.get('titulo') and request.POST.get('vigencia'):
                mensagem_possui_projeto = 'Se você não possui projeto, não pode escrever nada nos campos projeto, titulo e vigencia'
                return render(request, 'cad_docente.html', {'mensagem_possui_projeto': mensagem_possui_projeto})

            novo_docente.possui_projeto = request.POST.get('possui_projeto')
            novo_docente.info_projeto = ''

        elif request.POST.get('possui_projeto') == 'sim' and not request.POST.get('projeto') and not request.POST.get('titulo') and not request.POST.get('vigencia'):
            mensagem_possui_projeto = 'Se você possui projeto, precisa digitar nos campos projeto, titulo e vigencia'
            return render(request, 'cad_docente.html', {'mensagem_possui_projeto': mensagem_possui_projeto})

        lista_publi = request.POST.get('publicacoes')
        novo_docente.lista_publi = lista_publi
    
        login = preLogin.objects.get(email_inst=email, senha=senha)
        novo_docente.id_login = login

        request.session['login'] = login.id_pre_login

        novo_docente.save()
        request.session['chave'] = novo_docente.id_pre_cad_docente
    
    #elif perfil == "tecnico":
    #    novo_aluno_pos_dout = preCadPosDout()
    #    
    #    novo_aluno_pos_dout.nome = request.POST.get('nome')
    #    novo_aluno_pos_dout.celular = request.POST.get('tel')
    #    novo_aluno_pos_dout.email_inst = request.POST.get('email_inst')
    #    novo_aluno_pos_dout.senha = request.POST.get('senha')
    #    novo_aluno_pos_dout.matricula_ufabc = request.POST.get('matricula_ufabc')
    #    novo_aluno_pos_dout.ramal_lab = request.POST.get('lab')
    #    novo_aluno_pos_dout.nome_supervisor = request.POST.get('nome_supervisor')
    #    novo_aluno_pos_dout.centro = "centro ufabc"
    #    novo_aluno_pos_dout.data_pos = request.POST.get('data_inicio')
    #    novo_aluno_pos_dout.possui_bolsa = request.POST.get('bolsa')
    #    novo_aluno_pos_dout.programa_pos = "programa pos"
    #    novo_aluno_pos_dout.plano_trabalho = request.POST.get('plano_trabalho')
    #    novo_aluno_pos_dout.declaracao_ciencia_supervisor = request.POST.get('declaracao_supervisor')
    #    novo_aluno_pos_dout.save()
    #    request.session['chave'] = novo_aluno_pos_dout.id_pre_cad_pos_dout
   
    elif perfil == "aluno_pos_dout_ic":
        verifica_email = request.POST.get('email_inst')
        if Login.objects.filter(email_inst=verifica_email).exists():
            # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
            mensagem = 'O email que você digitou já possui cadastro'
            return render(request, 'cad_docente.html', {'mensagem': mensagem})

        if not request.session.get('recadastro'):
            email = request.POST.get('email_inst')
            senha = request.POST.get('senha')
            novo_login = preLogin()
            novo_login.email_inst = request.POST.get('email_inst')
            novo_login.senha = request.POST.get('senha')
            novo_login.perfil = 'aluno'
            novo_login.password_change_required = False
            novo_login.save()
        else:
            login = request.session.get('recadastro')
            user = Login.objects.get(id_login=login)
            user.perfil = 'docente'
            user.password_change_required = False
            user.save()

            email = user.email_inst
            senha = user.senha

            novo_login = preLogin()
            novo_login.email_inst = user.email_inst
            novo_login.senha = user.senha
            novo_login.perfil = user.perfil
            novo_login.password_change_required = user.password_change_required
            novo_login.save()

        novo_aluno_pos_ic = preCadAlunoPosIC()
        novo_aluno_pos_ic.primeiro_nome = request.POST.get('primeiro_nome')
        novo_aluno_pos_ic.segundo_nome = request.POST.get('segundo_nome')
        novo_aluno_pos_ic.celular = request.POST.get('tel')
        novo_aluno_pos_ic.matricula_ufabc = request.POST.get('matricula_ufabc')
        novo_aluno_pos_ic.ramal_lab = request.POST.get('lab')
        novo_aluno_pos_ic.nome_orientador = request.POST.get('nome_supervisor')
        novo_aluno_pos_ic.data_pos = request.POST.get('data_inicio')

        if request.POST.get('centro') == 'outro_centro':
            if request.POST.get('input_outro_centro'):

                novo_aluno_pos_ic.centro = request.POST.get('input_outro_centro')
            else:
                mensagem_outro_centro = 'Se você possui outro tipo de centro, precisa digitar qual é'
                return render(request, 'cad_aluno_pos_dout_ic.html', {'mensagem_outro_centro': mensagem_outro_centro})
        else:
            novo_aluno_pos_ic.centro = request.POST.get('centro')


        if request.POST.get('bolsa') == 'outra_bolsa':
            if request.POST.get('input_outra_bolsa'):

                novo_aluno_pos_ic.bolsa = request.POST.get('input_outra_bolsa')
            else:
                mensagem_outra_bolsa = 'Se você possui outro tipo de bolsa, precisa digitar qual é'
                return render(request, 'cad_aluno_pos_dout_ic.html', {'mensagem_outra_bolsa': mensagem_outra_bolsa})
        else:
            novo_aluno_pos_ic.bolsa = request.POST.get('bolsa')

        if request.POST.get('perfil') == 'outro_perfil':
            if request.POST.get('input_outro_perfil'):

                novo_aluno_pos_ic.perfil = request.POST.get('input_outro_perfil')
            else:
                mensagem_outro_perfil = 'Se você possui outro tipo de perfil, precisa digitar qual é'
                return render(request, 'cad_aluno_pos_dout_ic.html', {'mensagem_outro_perfil': mensagem_outro_perfil})
        else:
            novo_aluno_pos_ic.perfil = request.POST.get('perfil')
        
        
        novo_aluno_pos_ic.plano_trabalho = request.POST.get('plano_trabalho')
        novo_aluno_pos_ic.declaracao_ciencia_orientador = request.POST.get('declaracao_orientador')

        login = preLogin.objects.get(email_inst=email, senha=senha)
        novo_aluno_pos_ic.id_login = login

        request.session['login'] = login.id_pre_login

        novo_aluno_pos_ic.save()
        request.session['chave'] = novo_aluno_pos_ic.id_pre_cad_aluno_pos_ic
        return render(request, 'form_termo.html')
    
    elif perfil == "user_externo":

        if Login.objects.filter(request.POST.get('email_inst')).exists():
            # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
            mensagem = 'O email que você digitou já possui cadastro'
            return render(request, 'cad_user_externo.html', {'mensagem': mensagem})

        if not request.session.get('recadastro'):
            email = request.POST.get('email_inst')
            senha = request.POST.get('senha')
            novo_login = preLogin()
            novo_login.email_inst = request.POST.get('email_inst')
            novo_login.senha = request.POST.get('senha')
            novo_login.perfil = 'docente'
            novo_login.password_change_required = False
            novo_login.save()
        else:
            login = request.session.get('recadastro')
            user = Login.objects.get(id_login=login)
            user.perfil = 'user externo'
            user.password_change_required = False
            user.save()

            email = user.email_inst
            senha = user.senha

            novo_login = preLogin()
            novo_login.email_inst = user.email_inst
            novo_login.senha = user.senha
            novo_login.perfil = user.perfil
            novo_login.password_change_required = user.password_change_required
            novo_login.save()

            novo_login = preLogin()
            novo_login.email_inst = user.email_inst
            novo_login.senha = user.senha
            novo_login.perfil = user.perfil
            novo_login.password_change_required = user.password_change_required
            novo_login.save()

        novo_user_externo = preCadUserExterno()
        novo_user_externo.primeiro_nome = request.POST.get('primeiro_nome')
        novo_user_externo.segundo_nome = request.POST.get('segundo_nome')
        novo_user_externo.instituicao = request.POST.get('instituicao')
        novo_user_externo.atividade = request.POST.get('atividade')
        novo_user_externo.endereco_inst = request.POST.get('endereco_inst')
        novo_user_externo.celular = request.POST.get('tel')
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

        login = preLogin.objects.get(email_inst=email, senha=senha)
        novo_user_externo.id_login = login

        request.session['login'] = login.id_pre_login

        novo_user_externo.save()
        request.session['chave'] = novo_user_externo.id_pre_cad_user_externo

    chave = request.session.get('chave', 'valor_padrão')
    
    return render(request, 'form_termo.html')

def cadastrar_usuario(request):

    novo_termo = FormTermo()
    novo_termo.veracidade1 = request.POST.get('veracidade1')
    novo_termo.veracidade2 = request.POST.get('veracidade2')
    novo_termo.veracidade3 = request.POST.get('veracidade3')

    novo_termo.save()

    chave_termo = novo_termo.id_form_termo

    chave = request.session.get('chave', 'valor_padrão')
    perfil = request.session.get('perfil', 'valor_padrão')
    pre_login = request.session.get('login')

    if perfil == "docente":

        if not request.session.get('recadastro'):
            
            login = preLogin.objects.get(id_pre_login=pre_login)

            novo_login = Login()
            novo_login.email_inst = login.email_inst
            novo_login.senha = login.senha
            novo_login.perfil = login.perfil
            novo_login.password_change_required = False
            novo_login.save()
            login = Login.objects.get(email_inst=novo_login.email_inst, senha=novo_login.senha)

        else: 
            recadastro = request.session.get('recadastro')
            login = Login.objects.get(id_login=recadastro)

        docente = preCadDocente.objects.get(id_pre_cad_docente=chave)

        novo_docente = Docente()
        novo_docente.primeiro_nome = docente.primeiro_nome
        novo_docente.segundo_nome = docente.segundo_nome
        novo_docente.celular = docente.celular
        novo_docente.matricula_siape = docente.matricula_siape
        novo_docente.ramal_lab = docente.ramal_lab
        novo_docente.centro = docente.centro
        novo_docente.possui_projeto = docente.possui_projeto
        novo_docente.info_projeto = docente.info_projeto
        novo_docente.lista_publi = docente.lista_publi
        novo_docente.id_form_termo = novo_termo
        
        novo_docente.id_login = login
        novo_docente.save()
    
    #elif perfil == "pos_dout":
    #    pos_dout = preCadPosDout.objects.get(id_pre_cad_pos_dout=chave)
#
    #    if Docente.objects.filter(email_inst=pos_dout.email_inst).exists() or PosDout.objects.filter(email_inst=pos_dout.email_inst).exists() or AlunoPosIC.objects.filter(email_inst=pos_dout.email_inst).exists() or UserExterno.objects.filter(email_inst=pos_dout.email_inst).exists():
    #            # Trate o erro de e-mail duplicado, por exemplo, exiba uma mensagem de erro
    #        mensagem = 'O email que você digitou já possui cadastro'
    #        return render(request, 'cad_pos_dout.html', {'mensagem': mensagem})
#
    #    novo_pos_dout = PosDout()
    #    novo_pos_dout.nome = pos_dout.nome
    #    novo_pos_dout.celular = pos_dout.celular
    #    novo_pos_dout.email_inst = pos_dout.email_inst
    #    novo_pos_dout.senha = pos_dout.senha
    #    novo_pos_dout.matricula_ufabc = pos_dout.matricula_ufabc
    #    novo_pos_dout.ramal_lab = pos_dout.ramal_lab
    #    novo_pos_dout.nome_supervisor = pos_dout.nome_supervisor
    #    novo_pos_dout.centro = pos_dout.centro
    #    novo_pos_dout.data_pos = pos_dout.data_pos
    #    novo_pos_dout.possui_bolsa = pos_dout.possui_bolsa
    #    novo_pos_dout.programa_pos = pos_dout.programa_pos
    #    novo_pos_dout.plano_trabalho = pos_dout.plano_trabalho
    #    novo_pos_dout.declaracao_ciencia_supervisor = pos_dout.declaracao_ciencia_supervisor
    #    novo_pos_dout.id_form_termo = novo_termo
    #    novo_pos_dout.save()

    elif perfil == "aluno_pos_dout_ic":


        if not request.session.get('recadastro'):
                    
            login = preLogin.objects.get(id_pre_login=request.session.get('login'))

            novo_login = Login()
            novo_login.email_inst = login.email_inst
            novo_login.senha = login.senha
            novo_login.perfil = login.perfil
            novo_login.password_change_required = False
            novo_login.save()

        pos_dout_ic = preCadAlunoPosIC.objects.get(id_pre_cad_aluno_pos_ic=chave)

        novo_pos_dout_ic = AlunoPosIC()
        novo_pos_dout_ic.primeiro_nome = pos_dout_ic.primeiro_nome
        novo_pos_dout_ic.segundo_nome = pos_dout_ic.segundo_nome
        novo_pos_dout_ic.celular = pos_dout_ic.celular
        novo_pos_dout_ic.matricula_ufabc = pos_dout_ic.matricula_ufabc
        novo_pos_dout_ic.ramal_lab = pos_dout_ic.ramal_lab
        novo_pos_dout_ic.nome_orientador = pos_dout_ic.nome_orientador
        novo_pos_dout_ic.perfil = pos_dout_ic.perfil
        novo_pos_dout_ic.data_pos = pos_dout_ic.data_pos
        novo_pos_dout_ic.centro = pos_dout_ic.centro
        novo_pos_dout_ic.bolsa = pos_dout_ic.bolsa
        novo_pos_dout_ic.plano_trabalho = pos_dout_ic.plano_trabalho
        novo_pos_dout_ic.declaracao_ciencia_orientador = pos_dout_ic.declaracao_ciencia_orientador
        novo_pos_dout_ic.id_form_termo = novo_termo
        login = Login.objects.get(email_inst=novo_login.email_inst, senha=novo_login.senha)
        novo_pos_dout_ic.id_login = login
        novo_pos_dout_ic.save()

    elif perfil == "user_externo":


        if not request.session.get('recadastro'):
            
            login = preLogin.objects.get(id_pre_login=request.session.get('login'))

            novo_login = Login()
            novo_login.email_inst = login.email_inst
            novo_login.senha = login.senha
            novo_login.perfil = login.perfil
            novo_login.password_change_required = False
            novo_login.save()

        user_externo = preCadUserExterno.objects.get(id_pre_cad_user_externo=chave)

        novo_user_externo = UserExterno()
        novo_user_externo.primeiro_nome = user_externo.primeiro_nome
        novo_user_externo.segundo_nome = user_externo.segundo_nome
        novo_user_externo.instituicao = user_externo.instituicao
        novo_user_externo.atividade = user_externo.atividade
        novo_user_externo.endereco_inst = user_externo.endereco_inst
        novo_user_externo.celular = user_externo.celular
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
        login = Login.objects.get(email_inst=novo_login.email_inst, senha=novo_login.senha)
        novo_user_externo.id_login = login
        novo_user_externo.save()

    return redirect('encerrar_sessao')

def cad_aluno_pos_dout_ic(request):
    return render(request, 'cad_aluno_pos_dout_ic.html')
    
def cad_user_externo(request):
    return render(request, 'cad_user_externo.html')

def login_user(request):
    return render(request, 'index.html')

def verifica_login_user(request):
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if Login.objects.get(email_inst=email, senha=senha):
        login = Login.objects.get(email_inst=email, senha=senha)
        request.session['chave'] = login.id_login
        
        if login.password_change_required==False:
            return redirect('perfil_user')
        elif login.password_change_required==True:
            return render(request, 'redefinir_senha.html')
    
    else:
        mensagem = 'Email ou senha incorretos'
        return render(request, 'index.html', {'mensagem': mensagem})

def perfil_user(request):
 
    chave = request.session['chave']
    login = Login.objects.get(id_login=chave)

    if login.perfil == 'docente':
        user = Docente.objects.get(id_login=chave)
        #return render(request, 'perfil_user.html', {'docente': docente})
    
    elif login.perfil == 'pos_doutorando':
        user = PosDout.objects.get(id_pos_dout=chave)
        #return render(request, 'perfil_user.html', {'pos_doutorando': pos_doutorando})
    
    elif login.perfil == 'aluno_pos_ic':
        user = AlunoPosIC.objects.get(id_login=chave)
        #return render(request, 'perfil_user.html', {'aluno_pos_ic': aluno_pos_ic})

    elif login.perfil == 'user_externo':
        user = UserExterno.objects.get(id_login=chave)
        #return render(request, 'perfil_user.html', {'user_externo': user_externo})
    
    return render(request, 'perfil_user.html', {'user': user})
    
def encerrar_sessao(request):
    request.session.flush()
    return redirect(home)

def redefinir_senha(request):
    return render(request, 'redefinir_senha.html')

def confirma_redefinicao(request):
    senha_atual = request.POST.get('senha_atual')
    nova_senha = request.POST.get('nova_senha')
    confirma_nova_senha = request.POST.get('confirma_nova_senha')

    chave = request.session.get('chave')

    login = Login.objects.get(id_login=chave)

    if login.senha == senha_atual and nova_senha == confirma_nova_senha:
        login.senha = nova_senha
        login.save()
        request.session.flush()
        request.session['recadastro'] = login.id_login
        return render(request, 'form_perfil.html')
    
    else:
        mensagem_nova_senha = 'Senha atual incorreta ou nova senha confirmação incorreta'
        return render(request, 'cad_user_externo.html', {'mensagem_nova_senha': mensagem_nova_senha})

