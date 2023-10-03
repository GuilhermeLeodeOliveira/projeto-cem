from django.urls import path 
from .views import cad_equipamento
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cad_equipamento/', cad_equipamento, name='cad_equipamento')
]
