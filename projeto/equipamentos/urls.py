from django.urls import path 
from .views import cad_equipamento, equipamentos, cadastrar_equipamento
from . import views

urlpatterns = [
    path('cad_equipamento/', cad_equipamento, name='cad_equipamento'),
    path('cadastrar_equipamento/', cadastrar_equipamento, name='cadastrar_equipamento'),
    path('equipamentos/', equipamentos, name='equipamentos')
]
