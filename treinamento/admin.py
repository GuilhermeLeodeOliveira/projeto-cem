from django.contrib import admin
from .models import Solicitacoes, Treinamento, Prova, Palestra
# Register your models here.
admin.site.register(Solicitacoes)
admin.site.register(Treinamento)
admin.site.register(Prova)
admin.site.register(Palestra)