from django.contrib import admin
from django.urls import path, include
from .views import salvar, editar, update, delete, cadastro, formPerfil
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('cadastro/', cadastro, name='cadastro'),
    path('formPerfil/', formPerfil, name='formPerfil'),

]