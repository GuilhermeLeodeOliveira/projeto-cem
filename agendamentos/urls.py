from django.urls import path
#from . import views
from .views import agendamentos, realizar_agendamento, agendamentos_user, verifica_perfil, dados_user
from . import views

urlpatterns = [
    path('agendamentos/', agendamentos, name='agendamentos'),
    path('agendamento/calendario_equipamento/<int:id_equipamento>/', views.calendario_equipamento, name='calendario_equipamento'),
    path('realizar_agendamento/', views.realizar_agendamento, name='realizar_agendamento'),
    path('agendamentos_user/', views.agendamentos_user, name='agendamentos_user'),
    path('agendamentos/verifica_perfil/<str:email>/', views.verifica_perfil, name='verifica_perfil'),
    path('agendamentos/dados_user/', views.dados_user, name='dados_user')
]