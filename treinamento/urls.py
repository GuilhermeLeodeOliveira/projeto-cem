from django.urls import path 
#from . import views
from .views import treinamento, solicitacoes, solicitar_treinamento, solicitacoes_user, agendar_treinamento, finalizar_treinamento, concluir_treinamento

urlpatterns = [
    path('treinamento/', treinamento, name='treinamento'),
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('solicitar_treinamento/', solicitar_treinamento, name='solicitar_treinamento'),
    path('solicitacoes_user/', solicitacoes_user, name='solicitacoes_user'),
    path('agendar_treinamento/', agendar_treinamento, name='agendar_treinamento'),
    path('finalizar_treinamento/', finalizar_treinamento, name='finalizar_treinamento'),
    path('concluir_treinamento/', concluir_treinamento, name='concluir_treinamento'),
]