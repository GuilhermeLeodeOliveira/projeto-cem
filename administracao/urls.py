from django.urls import path, include
from .views import login_adm, verifica_login, dashboard, perfil_tecnico, encerrar_sessao_adm
from . import views

urlpatterns = [
    path('login_adm/', login_adm, name='login_adm'),
    path('verifica_login/', verifica_login, name='verifica_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('perfil_tecnico/', perfil_tecnico, name='perfil_tecnico'),
    path('encerrar_sessao_adm/', encerrar_sessao_adm, name='encerrar_sessao_adm'),
    path('solicitacoes/', include('treinamento.urls'), name='solicitacoes'),


]
