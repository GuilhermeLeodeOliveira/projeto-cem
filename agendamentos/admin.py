from django.contrib import admin
from .models import Agendamento, Dia, Mes
# Register your models here.

admin.site.register(Agendamento)
admin.site.register(Dia)
admin.site.register(Mes)