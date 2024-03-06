from django.urls import path 
#from . import views
from .views import treinamento, solicitacoes, solicitar_treinamento, solicitacoes_user, finalizar_palestra
from .views import agendar_treinamento, finalizar_treinamento, concluir_treinamento, agendar_palestra
from .views import gerar_csv, concluir_agendamento, agendar_prova, finalizar_prova, concluir_prova, concluir_palestra

urlpatterns = [
    path('treinamento/', treinamento, name='treinamento'),
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('solicitar_treinamento/', solicitar_treinamento, name='solicitar_treinamento'),
    path('solicitacoes_user/', solicitacoes_user, name='solicitacoes_user'),
    path('agendar_treinamento/', agendar_treinamento, name='agendar_treinamento'),
    path('finalizar_treinamento/', finalizar_treinamento, name='finalizar_treinamento'),
    path('concluir_treinamento/', concluir_treinamento, name='concluir_treinamento'),
    path('gerar_csv/', gerar_csv, name='gerar_csv'),
    path('concluir_agendamento/', concluir_agendamento, name='concluir_agendamento'),
    path('agendar_prova/', agendar_prova, name='agendar_prova'),
    path('finalizar_prova/', finalizar_prova, name='finalizar_prova'),
    path('concluir_prova/', concluir_prova, name='concluir_prova'),
    path('agendar_palestra/', agendar_palestra, name='agendar_palestra'),
    path('finalizar_palestra/', finalizar_palestra, name='finalizar_palestra'),
    path('concluir_palestra/', concluir_palestra, name='concluir_palestra')
]
