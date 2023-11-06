from django.urls import path 
#from . import views
from .views import treinamento, solicitacoes, solicitar_treinamento, solicitacoes_user

urlpatterns = [
    path('treinamento/', treinamento, name='treinamento'),
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('solicitar_treinamento/', solicitar_treinamento, name='solicitar_treinamento'),
    path('solicitacoes_user/', solicitacoes_user, name='solicitacoes_user'),
]