from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('administracao/', include('administracao.urls')),
    path('agendamentos/', include('agendamentos.urls')),
    
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
