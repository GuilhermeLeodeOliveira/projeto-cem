from django.urls import path 
from .views import login_adm
from . import views

urlpatterns = [
    path('login_adm/', login_adm, name='login_adm')
]
