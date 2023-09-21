from django.urls import path
from app_projeto_cem import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    #rota, view responsavel, nome de referência

    #projeto.com
    path('',views.home,name='index'),

    #projeto.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')

]

