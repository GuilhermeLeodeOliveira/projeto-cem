from django.contrib import admin
from .models import Agendamento, Dia, Mes, RegraAgendamento
# Register your models here.

admin.site.register(Agendamento)
admin.site.register(Dia)
admin.site.register(Mes)
admin.site.register(RegraAgendamento)