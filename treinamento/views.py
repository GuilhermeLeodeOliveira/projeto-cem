import csv
from django.template import loader, Context

from datetime import datetime
from django.shortcuts import render, redirect, reverse
#from .models import 
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from equipamentos.models import Equipamento
from core.models import Docente, AlunoPosIC, UserExterno, Login
from .models import Solicitacoes, Treinamento, Prova, Palestra
from administracao.models import Tecnico

# Create your views here.

def treinamento(request):
    if 'chave' in request.session:
        # Obtenha o ID do usuário atualmente logado
        chave = request.session.get('chave')
        login = Login.objects.get(id_login=chave)
        

        # Verifique o tipo de perfil e obtenha as solicitações correspondentes
        if login.perfil == 'docente':
            user = Docente.objects.get(id_login=chave)
            solicitacoes_usuario = Solicitacoes.objects.filter(id_login=login)
        elif login.perfil == 'pos_doutorando':
            solicitacoes_usuario = Solicitacoes.objects.filter(id_PosDout=chave)
        elif login.perfil == 'aluno' or login.perfil == 'aluno ou pos doc':
            user = AlunoPosIC.objects.get(id_login=chave)
            solicitacoes_usuario = Solicitacoes.objects.filter(id_login=login)
        elif login.perfil == 'user_externo':
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
    
    if 'chave' in request.session:
        chave = request.session['chave']
        login = Login.objects.get(id_login=chave)
        solicitacoes = Solicitacoes.objects.all()

        for solicitacao in solicitacoes:
            aluno_associado = None

            # Verificando se a solicitação está associada a um aluno
            if solicitacao.id_login.perfil == 'aluno ou pos doc':
                aluno_associado = AlunoPosIC.objects.filter(id_login=solicitacao.id_login).first()
                solicitacao.aluno_nome = aluno_associado.primeiro_nome if aluno_associado else None
            elif solicitacao.id_login.perfil == 'docente':
                docente_associado = Docente.objects.filter(id_login=solicitacao.id_login).first()
                solicitacao.docente_nome = docente_associado.primeiro_nome if docente_associado else None

            #solicitacao.aluno_nome = aluno_associado.primeiro_nome if aluno_associado else None

        equipamentos = Equipamento.objects.all()
        return render(request, 'solicitacoes.html', {'equipamentos': equipamentos, 'solicitacoes': solicitacoes})


def solicitar_treinamento(request):
    
    if request.method == 'POST':
        
        equipamentos_selecionados = request.POST.getlist('equipamento_selecionado')

        chave = request.session['chave']
        login = Login.objects.get(id_login=chave)
        
        for equipamento_nome in equipamentos_selecionados:
            
            # Verifique se já existe uma solicitação para o usuário e o equipamento
            usuario = None

            

            equipamento = Equipamento.objects.get(nome=equipamento_nome)

            if Solicitacoes.objects.filter(id_login=login, **{'id_equipamento': equipamento}).exists():
                # Já existe uma solicitação para esse usuário e equipamento
                # Você pode decidir o que fazer aqui, redirecionar para uma página de erro, etc.
                return HttpResponse('Você já realizou uma solicitação para esse equipamento')


            # Crie uma instância do modelo Equipamento para cada equipamento selecionado
            equipamento = Equipamento.objects.get(nome=equipamento_nome)
            nova_solicitacao = Solicitacoes()

            # Obtém a data e hora atuais
            data_hora_atual = datetime.now()

            # Separa a data e a hora
            data_atual = data_hora_atual.date()
            hora_atual = data_hora_atual.time()

            nova_solicitacao.data = data_atual
            nova_solicitacao.hora = hora_atual
            nova_solicitacao.status = 'pendente'

            chave = request.session['chave']

            nova_solicitacao.id_login = login                

            nova_solicitacao.id_equipamento = equipamento

            nova_solicitacao.save()  # Salve a instância no banco de dados

        # Redirecione para uma página de confirmação ou outra ação desejada
    return redirect('solicitacoes_user')


def solicitacoes_user(request):
    
    chave = request.session['chave']
    login = Login.objects.get(id_login=chave)

    solicitacoes = Solicitacoes.objects.filter(id_login=login)        
    treinamento = Treinamento.objects.filter(id_login_usuario=login)

    return render(request, 'solicitacoes_user.html', {'solicitacoes': solicitacoes, 'treinamento': treinamento})

def gerar_csv(request):

    if request.method == "POST":
        usuarios_selecionados = []

        # Verifique se a chave "usuario" existe nos dados POST
        if "usuario" in request.POST:
            # Separe os valores com base no caractere "_"
            valores_usuarios = request.POST.getlist("usuario")
            nome = None

            for valor in valores_usuarios:
                
                email, equipamento = valor.split("_")  # Separe o nome do equipamento_id

                #solicitacao = Solicitacoes.objects.all()

                if Login.objects.filter(email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                    login = Login.objects.get(email_inst=email)
                    aluno_pos_ic = AlunoPosIC.objects.get(id_login=login.id_login)
                    nome = aluno_pos_ic.primeiro_nome
                    

                #elif Solicitacoes.objects.filter(id_UserExterno__nome=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                #    user_externo = UserExterno.objects.filter(nome=email).first()
                #    email = user_externo.email_inst
                    

                usuarios_selecionados.append([nome, email, equipamento])
                

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
        
        #return redirect(reverse('solicitacoes'))

def agendar_treinamento(request):
    if request.method == "POST":
        usuarios_selecionados = []

        # Verifique se a chave "usuario" existe nos dados POST
        if "usuario" in request.POST:
            # Separe os valores com base no caractere "_"
            valores_usuarios = request.POST.getlist("usuario")
            nome = None
            # Verificar se a solicitação existe e está pendente e se o equipamento tem prova
            agenda_palestra = False
            agenda_prova = False
            for valor in valores_usuarios:
                email, equipamento = valor.split("_")
                
                if Solicitacoes.objects.filter(id_equipamento__nome=equipamento, id_login__email_inst=email, status='palestra realizada').exists() and Equipamento.objects.get(nome=equipamento).tem_prova is True:
                    
                    agenda_prova = True
                    
                    if Login.objects.filter(email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                    
                        login = Login.objects.get(email_inst=email)
                        
                        try:
                            aluno_pos_ic = AlunoPosIC.objects.get(id_login=login)
                            nome = aluno_pos_ic.primeiro_nome
                        except AlunoPosIC.DoesNotExist:
                            aluno_pos_ic = None
                            nome = None

                        if aluno_pos_ic is None:
                            try:
                                docente = Docente.objects.get(id_login=login)
                                nome = docente.primeiro_nome
                            except Docente.DoesNotExist:
                                return HttpResponse("Usuário não encontrado")

                    usuarios_selecionados.append([nome, email, equipamento])
                    request.session['usuarios_selecionados'] = usuarios_selecionados
                
                elif Solicitacoes.objects.filter(id_equipamento__nome=equipamento, id_login__email_inst=email, status='pendente').exists() and Equipamento.objects.get(nome=equipamento).tem_palestra is True:
                    
                    agenda_palestra = True

                    if Login.objects.filter(email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                    
                        login = Login.objects.get(email_inst=email)
                        
                        try:
                            aluno_pos_ic = AlunoPosIC.objects.get(id_login=login)
                            nome = aluno_pos_ic.primeiro_nome
                        except AlunoPosIC.DoesNotExist:
                            aluno_pos_ic = None
                            nome = None

                        if aluno_pos_ic is None:
                            try:
                                docente = Docente.objects.get(id_login=login)
                                nome = docente.primeiro_nome
                            except Docente.DoesNotExist:
                                return HttpResponse("Usuário não encontrado")

                    usuarios_selecionados.append([nome, email, equipamento])
                    request.session['usuarios_selecionados'] = usuarios_selecionados
                
                    
                else:
                    
                    # Se ambas as condições são verdadeiras, continue com o restante do processamento
                    if Login.objects.filter(email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                        login = Login.objects.get(email_inst=email)
                        
                        try:
                            aluno_pos_ic = AlunoPosIC.objects.get(id_login=login)
                            nome = aluno_pos_ic.primeiro_nome
                        except AlunoPosIC.DoesNotExist:
                            aluno_pos_ic = None
                            nome = None

                        if aluno_pos_ic is None:
                            try:
                                docente = Docente.objects.get(id_login=login)
                                nome = docente.primeiro_nome
                            except Docente.DoesNotExist:
                                return HttpResponse("Usuário não encontrado")

                    usuarios_selecionados.append([nome, email, equipamento])
                    request.session['usuarios_selecionados'] = usuarios_selecionados
            if agenda_prova is True:    
                return render(request, 'agendar_prova.html', {'usuarios_selecionados': usuarios_selecionados})
            
            elif agenda_palestra is True:
                return render(request, 'agendar_palestra.html', {'usuarios_selecionados': usuarios_selecionados})

            else:
                return render(request, 'agendar_treinamento.html', {'usuarios_selecionados': usuarios_selecionados})

def agendar_palestra(request):
    if request.method == "POST":
        # Recupere a lista de usuários selecionados da sessão
        usuarios_selecionados = request.session.get('usuarios_selecionados', [])
        
        # Itere sobre os usuários selecionados e processe os dados
        for usuario in usuarios_selecionados:
            
            nova_palestra = Palestra()  # Inicialize um novo objeto para cada usuário
            nome = usuario[0]
            email = usuario[1]
            equipamento = usuario[2]
            
            # Obtenha os dados específicos do formulário para este usuário
            nova_palestra.data_inicio_palestra = request.POST.get(f'data_inicio_{nome}_{email}_{equipamento}')
            nova_palestra.data_termino_palestra = request.POST.get(f'data_termino_{nome}_{email}_{equipamento}')
            nova_palestra.hora_inicio_palestra = request.POST.get(f'inicio_{nome}_{email}_{equipamento}')
            nova_palestra.hora_termino_palestra = request.POST.get(f'termino_{nome}_{email}_{equipamento}')
            nova_palestra.info_adicional = request.POST.get(f'info_adicional_palestra_{nome}_{email}_{equipamento}')
            nova_palestra.local_palestra = request.POST.get(f'local_{nome}_{email}_{equipamento}')
            
            #if Solicitacoes.objects.filter(id_Docente__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
            #    docente = Docente.objects.get(nome=nome)
            #    novo_treinamento.id_Docente = docente
            #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_Docente__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'em processo'
            #        solicitacao.save()
            #    novo_treinamento.id_solicitacao=solicitacao
            
            if Solicitacoes.objects.filter(id_login__email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                login_usuario = Login.objects.get(email_inst=email)
                
                try:
                    aluno_pos_ic = AlunoPosIC.objects.get(id_login=login_usuario)
                    nome = aluno_pos_ic.primeiro_nome
                except AlunoPosIC.DoesNotExist:
                    aluno_pos_ic = None
                    nome = None

                if aluno_pos_ic is None:
                    try:
                        docente = Docente.objects.get(id_login=login_usuario)
                        nome = docente.primeiro_nome
                    except Docente.DoesNotExist:
                        # Tratar o caso em que nem AlunoPosIC nem Docente foram encontrados
                        return HttpResponse("Usuário não encontrado") 
                
                solicitacao = Solicitacoes.objects.get(id_login=login_usuario.id_login, id_equipamento__nome=equipamento)
                if solicitacao:
                    # Modifique o status da solicitação
                    solicitacao.status = 'em palestra'
                    solicitacao.save()
                nova_palestra.id_solicitacao=solicitacao
            
           #elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
           #    user_externo = UserExterno.objects.get(nome=nome)
           #    novo_treinamento.id_UserExterno = user_externo
           #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_UserExterno__email_inst=email, id_equipamento__nome=equipamento)
           #    if solicitacao:
           #        # Modifique o status da solicitação
           #        solicitacao.status = 'em processo'
           #        solicitacao.save()
           #    novo_treinamento.id_solicitacao=solicitacao

                equip = Equipamento.objects.get(nome=equipamento)
                nova_palestra.id_equipamento = equip
                nova_palestra.id_login_usuario = login_usuario

                chave = request.session['chave']
                if request.session['perfil'] == 'tecnico':  
                    tecnico = Tecnico.objects.get(id_login=chave)  

                    nova_palestra.id_tecnico = tecnico
                else:
                    return HttpResponse('um administrativo ainda não pode realizar um treinamento')

                nova_palestra.save()

            else:
                return HttpResponse('Erro interno, entre em contato com a CEM')
            
        # Limpe a lista de usuários selecionados da sessão após o processamento
        del request.session['usuarios_selecionados']
        # Adicione qualquer lógica adicional ou redirecionamento aqui
        
        return redirect('solicitacoes')  # Crie um template para exibir uma mensagem de sucesso, se necessário

    return HttpResponse('Método não permitido')

def finalizar_palestra(request):
    if request.method == "POST":
        usuarios_selecionados = []
        # Recupere a lista de usuários selecionados da sessão
        if "usuario" in request.POST:
            valores_usuarios = request.POST.getlist("usuario")
                
            for valor in valores_usuarios:
                
                email, equipamento = valor.split("_")
               
                if Palestra.objects.filter(id_login_usuario__email_inst=email).exists() and Palestra.objects.filter(id_equipamento__nome=equipamento).exists():
                    
                    login = Login.objects.get(email_inst=email)
                    solicitacao = Solicitacoes.objects.get(id_login = login.id_login, id_equipamento__nome = equipamento)
                    
                    if solicitacao.status == "em palestra":

                        try:
                            user = AlunoPosIC.objects.get(id_login=login)
                        except AlunoPosIC.DoesNotExist:
                            try:
                                user = Docente.objects.get(id_login=login)
                            except Docente.DoesNotExist:
                                # Lidar com o caso em que nem AlunoPosIC nem Docente foram encontrados
                                return HttpResponse('Erro! Você está tentando passar um usuário não cadastrado, entre em contato com a CEM!')

                        
                #elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_equipamento__nome=equipamento)
                #    if solicitacao.status == "em processo":
                #        user_externo = UserExterno.objects.filter(nome=nome).first()
                #        email = user_externo.email_inst


                usuarios_selecionados.append([user.primeiro_nome, email, equipamento])

            # Armazene a lista de usuários selecionados na sessão
            request.session['usuarios_selecionados'] = usuarios_selecionados

            return render(request, 'finalizar_palestra.html', {'usuarios_selecionados': usuarios_selecionados})


def concluir_palestra(request):
    if request.method == "POST":
        # Recupere a lista de usuários selecionados da sessão
        usuarios_selecionados = request.session.get('usuarios_selecionados', [])
        
        # Itere sobre os usuários selecionados e processe os dados
        for usuario in usuarios_selecionados:
            
            nome = usuario[0]
            email = usuario[1]
            equipamento = usuario[2]
            
            # Obtenha os dados específicos do formulário para este usuário
            
            compareceu = request.POST.get(f'compareceu_{nome}_{email}_{equipamento}')
            justificativa = request.POST.get(f'justificativa_{nome}_{email}_{equipamento}')
            aptidao = request.POST.get(f'aptidao_{nome}_{email}_{equipamento}')

            #if Treinamento.objects.filter(id_Docente__nome=nome).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
            #    treinamento = Treinamento.objects.get(id_Docente__nome=nome, id_equipamento__nome=equipamento)
            #    treinamento.compareceu = compareceu
            #    treinamento.justificativa = justificativa
            #    treinamento.aptidao = aptidao
            #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_Docente__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'finalizado'
            #        solicitacao.save()
            #    treinamento.save()
            
            if Palestra.objects.filter(id_login_usuario__email_inst=email).exists() and Palestra.objects.filter(id_equipamento__nome=equipamento).exists():
                
                palestra = Palestra.objects.get(id_login_usuario__email_inst=email, id_equipamento__nome=equipamento)
                palestra.compareceu = compareceu
                palestra.justificativa = justificativa
                palestra.aptidao = aptidao
                solicitacao = Solicitacoes.objects.get(id_login__email_inst=email, id_equipamento__nome=equipamento)
                if solicitacao:
                    # Modifique o status da solicitação
                    solicitacao.status = 'palestra realizada'
                    solicitacao.save()
                palestra.save()
            
            #elif Treinamento.objects.filter(id_UserExterno__nome=nome).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
            #    treinamento = Treinamento.objects.get(id_UserExterno__nome=nome, id_equipamento__nome=equipamento)
            #    treinamento.compareceu = compareceu
            #    treinamento.justificativa = justificativa
            #    treinamento.aptidao = aptidao
            #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_UserExterno__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'finalizado'
            #        solicitacao.save()
            #    treinamento.save()

            
            
        # Limpe a lista de usuários selecionados da sessão após o processamento
        del request.session['usuarios_selecionados']
        # Adicione qualquer lógica adicional ou redirecionamento aqui
        
        return redirect('solicitacoes')  # Crie um template para exibir uma mensagem de sucesso, se necessário

    return HttpResponse('Método não permitido')


def agendar_prova(request):
    if request.method == "POST":
        # Recupere a lista de usuários selecionados da sessão
        usuarios_selecionados = request.session.get('usuarios_selecionados', [])
        
        # Itere sobre os usuários selecionados e processe os dados
        for usuario in usuarios_selecionados:
            
            nova_prova = Prova()  # Inicialize um novo objeto para cada usuário
            nome = usuario[0]
            email = usuario[1]
            equipamento = usuario[2]
            
            # Obtenha os dados específicos do formulário para este usuário
            nova_prova.data_inicio_prova = request.POST.get(f'data_inicio{nome}_{email}_{equipamento}')
            nova_prova.data_termino_prova = request.POST.get(f'data_termino{nome}_{email}_{equipamento}')
            nova_prova.hora_inicio_prova = request.POST.get(f'inicio_{nome}_{email}_{equipamento}')
            nova_prova.hora_termino_prova = request.POST.get(f'termino_{nome}_{email}_{equipamento}')
            nova_prova.info_adicional = request.POST.get(f'info_adicional_prova_{nome}_{email}_{equipamento}')
            nova_prova.local_prova = request.POST.get(f'local_{nome}_{email}_{equipamento}')
            
            #if Solicitacoes.objects.filter(id_Docente__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
            #    docente = Docente.objects.get(nome=nome)
            #    novo_treinamento.id_Docente = docente
            #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_Docente__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'em processo'
            #        solicitacao.save()
            #    novo_treinamento.id_solicitacao=solicitacao
            
            if Solicitacoes.objects.filter(id_login__email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                login_usuario = Login.objects.get(email_inst=email)
                
                try:
                    aluno_pos_ic = AlunoPosIC.objects.get(id_login=login_usuario)
                    nome = aluno_pos_ic.primeiro_nome
                except AlunoPosIC.DoesNotExist:
                    aluno_pos_ic = None
                    nome = None

                if aluno_pos_ic is None:
                    try:
                        docente = Docente.objects.get(id_login=login_usuario)
                        nome = docente.primeiro_nome
                    except Docente.DoesNotExist:
                        # Tratar o caso em que nem AlunoPosIC nem Docente foram encontrados
                        return HttpResponse("Usuário não encontrado") 
                
                solicitacao = Solicitacoes.objects.get(id_login=login_usuario.id_login, id_equipamento__nome=equipamento)
                if solicitacao:
                    # Modifique o status da solicitação
                    solicitacao.status = 'em prova'
                    solicitacao.save()
                nova_prova.id_solicitacao=solicitacao
            
           #elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
           #    user_externo = UserExterno.objects.get(nome=nome)
           #    novo_treinamento.id_UserExterno = user_externo
           #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_UserExterno__email_inst=email, id_equipamento__nome=equipamento)
           #    if solicitacao:
           #        # Modifique o status da solicitação
           #        solicitacao.status = 'em processo'
           #        solicitacao.save()
           #    novo_treinamento.id_solicitacao=solicitacao

                equip = Equipamento.objects.get(nome=equipamento)
                nova_prova.id_equipamento = equip
                nova_prova.id_login_usuario = login_usuario

                chave = request.session['chave']
                if request.session['perfil'] == 'tecnico':  
                    tecnico = Tecnico.objects.get(id_login=chave)  

                    nova_prova.id_tecnico = tecnico
                else:
                    return HttpResponse('um administrativo ainda não pode realizar um treinamento')

                nova_prova.save()

            else:
                return HttpResponse('Erro interno, entre em contato com a CEM')
            
        # Limpe a lista de usuários selecionados da sessão após o processamento
        del request.session['usuarios_selecionados']
        # Adicione qualquer lógica adicional ou redirecionamento aqui
        
        return redirect('solicitacoes')  # Crie um template para exibir uma mensagem de sucesso, se necessário

    return HttpResponse('Método não permitido')

def finalizar_prova(request):
    if request.method == "POST":
        usuarios_selecionados = []
        # Recupere a lista de usuários selecionados da sessão
        if "usuario" in request.POST:
            valores_usuarios = request.POST.getlist("usuario")
                
            for valor in valores_usuarios:
                
                email, equipamento = valor.split("_")
                
                if Prova.objects.filter(id_login_usuario__email_inst=email).exists() and Prova.objects.filter(id_equipamento__nome=equipamento).exists():
                    
                    login = Login.objects.get(email_inst=email)
                    solicitacao = Solicitacoes.objects.get(id_login = login.id_login, id_equipamento__nome = equipamento)
                    
                    if solicitacao.status == "em prova":

                        try:
                            user = AlunoPosIC.objects.get(id_login=login)
                        except AlunoPosIC.DoesNotExist:
                            try:
                                user = Docente.objects.get(id_login=login)
                            except Docente.DoesNotExist:
                                # Lidar com o caso em que nem AlunoPosIC nem Docente foram encontrados
                                return HttpResponse('Erro! Você está tentando passar um usuário não cadastrado, entre em contato com a CEM!')

                        
                #elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_equipamento__nome=equipamento)
                #    if solicitacao.status == "em processo":
                #        user_externo = UserExterno.objects.filter(nome=nome).first()
                #        email = user_externo.email_inst


                usuarios_selecionados.append([user.primeiro_nome, email, equipamento])

            # Armazene a lista de usuários selecionados na sessão
            request.session['usuarios_selecionados'] = usuarios_selecionados

            return render(request, 'finalizar_prova.html', {'usuarios_selecionados': usuarios_selecionados})


def concluir_agendamento(request):
    if request.method == "POST":
        # Recupere a lista de usuários selecionados da sessão
        usuarios_selecionados = request.session.get('usuarios_selecionados', [])
        
        # Itere sobre os usuários selecionados e processe os dados
        for usuario in usuarios_selecionados:
            
            novo_treinamento = Treinamento()  # Inicialize um novo objeto para cada usuário
            nome = usuario[0]
            email = usuario[1]
            equipamento = usuario[2]
            
            # Obtenha os dados específicos do formulário para este usuário
            novo_treinamento.data_treinamento = request.POST.get(f'data_{nome}_{email}_{equipamento}')
            novo_treinamento.hora_inicio_treinamento = request.POST.get(f'inicio_{nome}_{email}_{equipamento}')
            novo_treinamento.hora_termino_treinamento = request.POST.get(f'termino_{nome}_{email}_{equipamento}')
            novo_treinamento.local_treinamento = request.POST.get(f'local_{nome}_{email}_{equipamento}')
            
            #if Solicitacoes.objects.filter(id_Docente__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
            #    docente = Docente.objects.get(nome=nome)
            #    novo_treinamento.id_Docente = docente
            #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_Docente__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'em processo'
            #        solicitacao.save()
            #    novo_treinamento.id_solicitacao=solicitacao
            
            if Solicitacoes.objects.filter(id_login__email_inst=email).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                login_usuario = Login.objects.get(email_inst=email)
                
                try:
                    aluno_pos_ic = AlunoPosIC.objects.get(id_login=login_usuario)
                    nome = aluno_pos_ic.primeiro_nome
                except AlunoPosIC.DoesNotExist:
                    aluno_pos_ic = None
                    nome = None

                if aluno_pos_ic is None:
                    try:
                        docente = Docente.objects.get(id_login=login_usuario)
                        nome = docente.primeiro_nome
                    except Docente.DoesNotExist:
                        # Tratar o caso em que nem AlunoPosIC nem Docente foram encontrados
                        return HttpResponse("Usuário não encontrado") 
                
                solicitacao = Solicitacoes.objects.get(id_login=login_usuario.id_login, id_equipamento__nome=equipamento)
                if solicitacao:
                    # Modifique o status da solicitação
                    solicitacao.status = 'em processo'
                    solicitacao.save()
                novo_treinamento.id_solicitacao=solicitacao
            
           #elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
           #    user_externo = UserExterno.objects.get(nome=nome)
           #    novo_treinamento.id_UserExterno = user_externo
           #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_UserExterno__email_inst=email, id_equipamento__nome=equipamento)
           #    if solicitacao:
           #        # Modifique o status da solicitação
           #        solicitacao.status = 'em processo'
           #        solicitacao.save()
           #    novo_treinamento.id_solicitacao=solicitacao

                equip = Equipamento.objects.get(nome=equipamento)
                novo_treinamento.id_equipamento = equip
                novo_treinamento.id_login_usuario = login_usuario

                chave = request.session['chave']
                if request.session['perfil'] == 'tecnico':    
                    tecnico = Tecnico.objects.get(id_login=chave)  

                    novo_treinamento.id_tecnico = tecnico
                else:
                    return HttpResponse('um administrativo ainda não pode realizar um treinamento')

                novo_treinamento.save()

            else:
                return HttpResponse('Erro interno, entre em contato com a CEM')
            
        # Limpe a lista de usuários selecionados da sessão após o processamento
        del request.session['usuarios_selecionados']
        # Adicione qualquer lógica adicional ou redirecionamento aqui
        
        return redirect('solicitacoes')  # Crie um template para exibir uma mensagem de sucesso, se necessário

    return HttpResponse('Método não permitido')


def concluir_prova(request):
    if request.method == "POST":
        # Recupere a lista de usuários selecionados da sessão
        usuarios_selecionados = request.session.get('usuarios_selecionados', [])
        
        # Itere sobre os usuários selecionados e processe os dados
        for usuario in usuarios_selecionados:
            
            nome = usuario[0]
            email = usuario[1]
            equipamento = usuario[2]
            
            # Obtenha os dados específicos do formulário para este usuário
            
            compareceu = request.POST.get(f'compareceu_{nome}_{email}_{equipamento}')
            justificativa = request.POST.get(f'justificativa_{nome}_{email}_{equipamento}')
            aptidao = request.POST.get(f'aptidao_{nome}_{email}_{equipamento}')

            #if Treinamento.objects.filter(id_Docente__nome=nome).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
            #    treinamento = Treinamento.objects.get(id_Docente__nome=nome, id_equipamento__nome=equipamento)
            #    treinamento.compareceu = compareceu
            #    treinamento.justificativa = justificativa
            #    treinamento.aptidao = aptidao
            #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_Docente__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'finalizado'
            #        solicitacao.save()
            #    treinamento.save()
            
            if Prova.objects.filter(id_login_usuario__email_inst=email).exists() and Prova.objects.filter(id_equipamento__nome=equipamento).exists():
                
                prova = Prova.objects.get(id_login_usuario__email_inst=email, id_equipamento__nome=equipamento)
                prova.compareceu = compareceu
                prova.justificativa = justificativa
                prova.aptidao = aptidao
                solicitacao = Solicitacoes.objects.get(id_login__email_inst=email, id_equipamento__nome=equipamento)
                if solicitacao:
                    # Modifique o status da solicitação
                    solicitacao.status = 'prova realizada'
                    solicitacao.save()
                prova.save()
            
            #elif Treinamento.objects.filter(id_UserExterno__nome=nome).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
            #    treinamento = Treinamento.objects.get(id_UserExterno__nome=nome, id_equipamento__nome=equipamento)
            #    treinamento.compareceu = compareceu
            #    treinamento.justificativa = justificativa
            #    treinamento.aptidao = aptidao
            #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_UserExterno__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'finalizado'
            #        solicitacao.save()
            #    treinamento.save()

            
            
        # Limpe a lista de usuários selecionados da sessão após o processamento
        if 'usuarios_selecionados' in request.session:
            del request.session['usuarios_selecionados']
        

        # Adicione qualquer lógica adicional ou redirecionamento aqui
        
        return redirect('solicitacoes')  # Crie um template para exibir uma mensagem de sucesso, se necessário

    return HttpResponse('Método não permitido')


def finalizar_treinamento(request):
    
    if request.method == "POST":
        usuarios_selecionados = []

        # Verifique se a chave "usuario" existe nos dados POST
        if "usuario" in request.POST:
            # Separe os valores com base no caractere "_"
            valores_usuarios = request.POST.getlist("usuario")
            
            for valor in valores_usuarios:
                
                email, equipamento = valor.split("_")  # Separe o nome do equipamento_id

                #solicitacao = Solicitacoes.objects.all()

                #if Solicitacoes.objects.filter(id_Docente__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_equipamento__nome = equipamento)
                #    if solicitacao.status == "em processo":
                #        docente = Docente.objects.filter(nome=nome).first()
                #        email = docente.email_inst
                        

                if Treinamento.objects.filter(id_login_usuario__email_inst=email).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
                    
                    login = Login.objects.get(email_inst=email)
                    solicitacao = Solicitacoes.objects.get(id_login = login.id_login, id_equipamento__nome = equipamento)
            
                    if solicitacao.status == "em processo":

                        try:
                            user = AlunoPosIC.objects.get(id_login=login)
                        except AlunoPosIC.DoesNotExist:
                            try:
                                user = Docente.objects.get(id_login=login)
                            except Docente.DoesNotExist:
                                # Lidar com o caso em que nem AlunoPosIC nem Docente foram encontrados
                                return HttpResponse('Erro! Você está tentando passar um usuário não cadastrado, entre em contato com a CEM!')

                        
                #elif Solicitacoes.objects.filter(id_UserExterno__nome=nome).exists() and Solicitacoes.objects.filter(id_equipamento__nome=equipamento).exists():
                #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_equipamento__nome=equipamento)
                #    if solicitacao.status == "em processo":
                #        user_externo = UserExterno.objects.filter(nome=nome).first()
                #        email = user_externo.email_inst


                usuarios_selecionados.append([user.primeiro_nome, email, equipamento])

            # Armazene a lista de usuários selecionados na sessão
            request.session['usuarios_selecionados'] = usuarios_selecionados

            return render(request, 'finalizar_treinamento.html', {'usuarios_selecionados': usuarios_selecionados})


def concluir_treinamento(request):
    print(request.POST)
    if request.method == "POST":
        # Recupere a lista de usuários selecionados da sessão
        usuarios_selecionados = request.session.get('usuarios_selecionados', [])
        
        # Itere sobre os usuários selecionados e processe os dados
        for usuario in usuarios_selecionados:
            
            nome = usuario[0]
            email = usuario[1]
            equipamento = usuario[2]
            
            # Obtenha os dados específicos do formulário para este usuário
            
            compareceu = request.POST.get(f'compareceu_{nome}_{email}_{equipamento}')
            justificativa = request.POST.get(f'justificativa_{nome}_{email}_{equipamento}')
            aptidao = request.POST.get(f'aptidao_{nome}_{email}_{equipamento}')

            #if Treinamento.objects.filter(id_Docente__nome=nome).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
            #    treinamento = Treinamento.objects.get(id_Docente__nome=nome, id_equipamento__nome=equipamento)
            #    treinamento.compareceu = compareceu
            #    treinamento.justificativa = justificativa
            #    treinamento.aptidao = aptidao
            #    solicitacao = Solicitacoes.objects.get(id_Docente__nome=nome, id_Docente__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'finalizado'
            #        solicitacao.save()
            #    treinamento.save()
            
            if Treinamento.objects.filter(id_login_usuario__email_inst=email).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
                
                treinamento = Treinamento.objects.get(id_login_usuario__email_inst=email, id_equipamento__nome=equipamento)
                treinamento.compareceu = compareceu
                treinamento.justificativa = justificativa
                treinamento.aptidao = aptidao
                solicitacao = Solicitacoes.objects.get(id_login__email_inst=email, id_equipamento__nome=equipamento)
                if solicitacao:
                    # Modifique o status da solicitação
                    solicitacao.status = 'finalizado'
                    solicitacao.save()
                treinamento.save()
            
            #elif Treinamento.objects.filter(id_UserExterno__nome=nome).exists() and Treinamento.objects.filter(id_equipamento__nome=equipamento).exists():
            #    treinamento = Treinamento.objects.get(id_UserExterno__nome=nome, id_equipamento__nome=equipamento)
            #    treinamento.compareceu = compareceu
            #    treinamento.justificativa = justificativa
            #    treinamento.aptidao = aptidao
            #    solicitacao = Solicitacoes.objects.get(id_UserExterno__nome=nome, id_UserExterno__email_inst=email, id_equipamento__nome=equipamento)
            #    if solicitacao:
            #        # Modifique o status da solicitação
            #        solicitacao.status = 'finalizado'
            #        solicitacao.save()
            #    treinamento.save()

            
            
        # Limpe a lista de usuários selecionados da sessão após o processamento
        del request.session['usuarios_selecionados']
        # Adicione qualquer lógica adicional ou redirecionamento aqui
        
        return redirect('solicitacoes')  # Crie um template para exibir uma mensagem de sucesso, se necessário

    return HttpResponse('Método não permitido')