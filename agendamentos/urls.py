from django.urls import path 
#from . import views
from .views import agendamentos
from . import views

urlpatterns = [
    path('agendamentos/', agendamentos, name='agendamentos'),
    path('agendamento/calendario_equipamento/<int:id_equipamento>/', views.calendario_equipamento, name='calendario_equipamento')

]