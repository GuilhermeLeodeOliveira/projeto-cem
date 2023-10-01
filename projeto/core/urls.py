from django.contrib import admin
from django.urls import path, include
from .views import salvar, editar, update, delete, cadastro, form_perfil, selecionar_tela, cad_docente, form_infra, form_termo, cadastrar_usuario
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('cadastro/', cadastro, name='cadastro'),
    path('form_perfil/', form_perfil, name='form_perfil'),
    path('selecionar_tela/', selecionar_tela, name='selecionar_tela'),
    path('cad_docente/', cad_docente, name='cad_docente'),
    path('form_infra/', form_infra, name='form_infra'),
    path('form_termo/', form_termo, name='form_termo'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),

]