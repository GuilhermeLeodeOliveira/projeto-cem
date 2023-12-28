from django.urls import path 
#from . import views
from .views import agendamentos
from . import views

urlpatterns = [
    path('agendamentos/', agendamentos, name='agendamentos'),

]