from django.contrib import admin
from .models import Agendamento, DiaOff, Calendario
# Register your models here.

admin.site.register(Agendamento)
admin.site.register(DiaOff)
admin.site.register(Calendario)