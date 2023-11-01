from django.urls import path 
from .views import treinamento
from . import views

urlpatterns = [
    path('treinamento/', treinamento, name='treinamento'),
    
]