from django.urls import path 
#from . import views
from .views import agendamentos, realizar_agendamento
from . import views

urlpatterns = [
    path('agendamentos/', agendamentos, name='agendamentos'),
    path('agendamento/calendario_equipamento/<int:id_equipamento>/', views.calendario_equipamento, name='calendario_equipamento'),
    path('realizar_agendamento/', views.realizar_agendamento, name='realizar_agendamento')
]