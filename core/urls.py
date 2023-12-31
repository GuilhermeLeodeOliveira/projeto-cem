from django.contrib import admin
from django.urls import path, include
from .views import salvar, editar, update, delete, cadastro, form_perfil, selecionar_tela, edita_dados_user
from .views import cad_docente, form_termo, cadastrar_usuario, cad_aluno_pos_dout_ic, confirma_redefinicao
from .views import cad_user_externo, login_user, verifica_login_user, perfil_user, encerrar_sessao, redefinir_senha
from .views import editando_dados, troca_senha, trocando_senha
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('cadastro/', cadastro, name='cadastro'),
    path('form_perfil/', form_perfil, name='form_perfil'),
    path('selecionar_tela/', selecionar_tela, name='selecionar_tela'),
    path('cad_docente/', cad_docente, name='cad_docente'),
    path('form_termo/', form_termo, name='form_termo'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cad_aluno_pos_dout_ic/', cad_aluno_pos_dout_ic, name='cad_aluno_pos_dout_ic'),
    path('cad_user_externo/', cad_user_externo, name='cad_user_externo'),
    path('login_user/', login_user, name='login_user'),
    path('perfil_user/', perfil_user, name='perfil_user'),
    path('verifica_login_user/', verifica_login_user, name='verifica_login_user'),
    path('encerrar_sessao/', encerrar_sessao, name='encerrar_sessao'),
    path('equipamentos/', include('equipamentos.urls'), name='cad_equipamento'),
    path('treinamento/', include('treinamento.urls'), name='treinamento'),
    path('solicitacoes_user/', include('treinamento.urls'), name='solicitacoes_user'),
    path('confirma_redefinicao/', confirma_redefinicao, name='confirma_redefinicao'),
    path('redefinir_senha/', redefinir_senha, name='redefinir_senha'),
    path('edita_dados_user/', edita_dados_user, name='edita_dados_user'),
    path('editando_dados/', editando_dados, name='editando_dados'),
    path('troca_senha/', troca_senha, name='troca_senha'),
    path('trocando_senha/', trocando_senha, name='trocando_senha'),
    path('agendamentos/', include('agendamentos.urls'), name='agendamentos'),

]