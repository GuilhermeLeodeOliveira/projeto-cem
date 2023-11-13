import csv
from django.template import loader, Context

from datetime import datetime
from django.shortcuts import render, redirect
#from .models import 
from django.http import HttpResponse
from django.http import JsonResponse
from equipamentos.models import Equipamento
from core.models import Docente, PosDout, AlunoPosIC, UserExterno
from .models import Solicitacoes


# Create your views here.

def treinamento(request):
    if 'chave' in request.session:
        # Obtenha o ID do usuário atualmente logado
        perfil_user = request.session.get('perfil')
        chave = request.session.get('chave')

        # Verifique o tipo de perfil e obtenha as solicitações correspondentes
        if perfil_user == 'docente':
            solicitacoes_usuario = Solicitacoes.objects.filter(id_Docente=chave)
        elif perfil_user == 'pos_doutorando':
            solicitacoes_usuario = Solicitacoes.objects.filter(id_PosDout=chave)
        elif perfil_user == 'aluno_pos_ic':
            solicitacoes_usuario = Solicitacoes.objects.filter(id_AlunoPosIC=chave)
        elif perfil_user == 'user_externo':
            solicitacoes_usuario = Solicitacoes.objects.filter(id_UserExterno=chave)
        else:
            solicitacoes_usuario = None

        # Se houver solicitações para o usuário, exclua os equipamentos associados a essas solicitações
        if solicitacoes_usuario:
            equipamentos = Equipamento.objects.exclude(id_equipamento__in=solicitacoes_usuario.values('id_equipamento'))
        else:
            equipamentos = Equipamento.objects.all()
        return render(request, 'treinamento.html', {'equipamentos': equipamentos})
    else:
        return HttpResponse('Precisa estar logado para acessar essa função')
    

def solicitacoes(request):
    perfil = request.session['perfil']
    if 'chave' in request.session:
        chave = request.session['chave']
        solicitacoes = Solicitacoes.objects.filter(id_equipamento__id_tecnico=chave)
        equipamentos = Equipamento.objects.filter(id_tecnico = chave)
        return render(request, 'solicitacoes.html', {'perfil': perfil, 'equipamentos':equipamentos, 'solicitacoes': solicitacoes})

def solicitar_treinamento(request):
    
    if request.method == 'POST':
        
        equipamentos_selecionados = request.POST.getlist('equipamento_selecionado')

        perfil_user = request.session['perfil']
        chave = request.session['chave']
        
        for equipamento_nome in equipamentos_selecionados:
            
            # Verifique se já existe uma solicitação para o usuário e o equipamento
            usuario = None

            if perfil_user == 'docente':
                usuario = Docente.objects.get(id_docente=chave)
                campo_usuario = 'id_Docente'
            elif perfil_user == 'pos_doutorando':
                usuario = PosDout.objects.get(id_pos_dout=chave)
                campo_usuario = 'id_PosDout'
            elif perfil_user == 'aluno_pos_ic':
                usuario = AlunoPosIC.objects.get(id_aluno_pos_ic=chave)
                campo_usuario = 'id_AlunoPosIC'
            elif perfil_user == 'user_externo':
                usuario = UserExterno.objects.get(id_user_externo=chave)
                campo_usuario = 'id_UserExterno'

            equipamento = Equipamento.objects.get(nome=equipamento_nome)

            if Solicitacoes.objects.filter(**{campo_usuario: usuario, 'id_equipamento': equipamento}).exists():
                # Já existe uma solicitação para esse usuário e equipamento
                # Você pode decidir o que fazer aqui, redirecionar para uma página de erro, etc.
                return HttpResponse('Você já realizou uma solicitação para esse equipamento')


            # Crie uma instância do modelo Equipamento para cada equipamento selecionado
            equipamento = Equipamento.objects.get(nome=equipamento_nome)
            nova_solicitacao = Solicitacoes()
            nova_solicitacao.data = request.POST.get('nome')

            # Obtém a data e hora atuais
            data_hora_atual = datetime.now()

            # Separa a data e a hora
            data_atual = data_hora_atual.date()
            hora_atual = data_hora_atual.time()

            nova_solicitacao.data = data_atual
            nova_solicitacao.hora = hora_atual
            nova_solicitacao.status = 'pendente'

            perfil_user = request.session['perfil']
            chave = request.session['chave']

            if perfil_user == 'docente':
                docente = Docente.objects.get(id_docente=chave)
                nova_solicitacao.id_Docente = docente
                
            elif perfil_user == 'pos_doutorando':
                pos_dout = PosDout.objects.get(id_pos_dout=chave)
                nova_solicitacao.id_PosDout = pos_dout
                
            elif perfil_user == 'aluno_pos_ic':

                aluno_pos_ic = AlunoPosIC.objects.get(id_aluno_pos_ic=chave)
                nova_solicitacao.id_AlunoPosIC = aluno_pos_ic
                
            elif perfil_user == 'user_externo':
                user_externo = UserExterno.objects.get(id_user_externo=chave)
                nova_solicitacao.id_UserExterno = user_externo
                

            nova_solicitacao.id_equipamento = equipamento

            nova_solicitacao.save()  # Salve a instância no banco de dados

        # Redirecione para uma página de confirmação ou outra ação desejada
    return render(request, 'perfil_user.html')


def solicitacoes_user(request):

    perfil_user = request.session['perfil']
    chave = request.session['chave']

    if perfil_user == 'docente':
        solicitacoes = Solicitacoes.objects.filter(id_Docente=chave)
        
        
    elif perfil_user == 'pos_doutorando':
        solicitacoes = Solicitacoes.objects.filter(id_PosDout=chave)
        
        
    elif perfil_user == 'aluno_pos_ic':
        solicitacoes = Solicitacoes.objects.filter(id_AlunoPosIC=chave)
        
        
    elif perfil_user == 'user_externo':
        solicitacoes = Solicitacoes.objects.filter(id_UserExterno=chave)
        
    return render(request, 'solicitacoes_user.html', {'solicitacoes': solicitacoes})

def agendar_treinamento(request):

    if request.method == "POST":
        usuarios_selecionados = []

        # Verifique se a chave "usuario" existe nos dados POST
        if "usuario" in request.POST:
            # Separe os valores com base no caractere "_"
            valores_usuarios = request.POST.getlist("usuario")
            

            for valor in valores_usuarios:
                
                nome, equipamento_id = valor.split("_")  # Separe o nome do equipamento_id

                #solicitacao = Solicitacoes.objects.all()
                
                if Solicitacoes.objects.filter(id_Docente__nome=nome).exists():
                    docente = Docente.objects.filter(nome=nome).first()
                    email = docente.email_inst

                elif Solicitacoes.objects.filter(id_PosDout__nome=nome).exists():
                    docente = PosDout.objects.filter(nome=nome).first()
                    email = docente.email_inst


                elif Solicitacoes.objects.filter(id_AlunoPosIC__nome=nome).exists():
                    docente = AlunoPosIC.objects.filter(nome=nome).first()
                    email = docente.email_inst


                elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists():
                    docente = UserExterno.objects.filter(nome=nome).first()
                    email = docente.email_inst

                usuarios_selecionados.append([nome, email, equipamento_id])
                

            # Criar um arquivo CSV com os dados coletados
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="usuarios_selecionados.csv"'

            # Crie um objeto CSV com quoting definido como QUOTE_MINIMAL
            writer = csv.writer(response, delimiter=",", quoting=csv.QUOTE_MINIMAL)

            # Escreva o cabeçalho
            writer.writerow(["Nome do Usuário", "Email", "Equipamento"])
            

            # Escreva os dados
            for usuario in usuarios_selecionados:
                writer.writerow(usuario)
                            
            # Obtenha o conteúdo da resposta como uma string
            csv_data = response.content.decode('utf-8')
            response.content = csv_data.encode('utf-16')

            return response

    return HttpResponse("Requisição inválida")


def finalizar_treinamento(request):
    return HttpResponse('funciona')

def concluir_treinamento(request):
    return HttpResponse('funciona')