from django.urls import path 
from .views import login_adm, verifica_login, dashboard
from . import views

urlpatterns = [
    path('login_adm/', login_adm, name='login_adm'),
    path('verifica_login/', verifica_login, name='verifica_login'),
    path('dashboard/', dashboard, name='dashboard'),

]
