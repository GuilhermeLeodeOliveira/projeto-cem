from django.urls import path, include
from .views import login_adm, verifica_login, dashboard, perfil_tecnico, encerrar_sessao_adm, edita_dados_tecnico
from .views import editando_dados_tecnico, form_calendario, visualizar_info_user
from . import views

urlpatterns = [
    path('login_adm/', login_adm, name='login_adm'),
    path('agendamento/visualizar_info_user/<int:id_login>/', views.visualizar_info_user, name='visualizar_info_user'),
    path('verifica_login/', verifica_login, name='verifica_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('perfil_tecnico/', perfil_tecnico, name='perfil_tecnico'),
    path('encerrar_sessao_adm/', encerrar_sessao_adm, name='encerrar_sessao_adm'),
    path('solicitacoes/', include('treinamento.urls'), name='solicitacoes'),
    path('edita_dados_tecnico/', edita_dados_tecnico, name='edita_dados_tecnico'),
    path('editando_dados_tecnico/', editando_dados_tecnico, name='editando_dados_tecnico'),
    path('form_calendario/', form_calendario, name='form_calendario'),

]
