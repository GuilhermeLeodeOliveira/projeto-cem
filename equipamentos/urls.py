from django.urls import path 
from .views import cad_equipamento, equipamentos, cadastrar_equipamento
from . import views

urlpatterns = [
    path('cad_equipamento/', cad_equipamento, name='cad_equipamento'),
    path('cadastrar_equipamento/', cadastrar_equipamento, name='cadastrar_equipamento'),
    path('equipamentos/', equipamentos, name='equipamentos'),
    path('equipamento/editar/<int:id_equipamento>/', views.editar_equipamento, name='editar_equipamento'),
    path('equipamento/salvar_edicao/<int:id_equipamento>/', views.salvar_edicao_equipamento, name='salvar_edicao_equipamento')


]
