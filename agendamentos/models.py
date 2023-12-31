from django.db import models
import datetime
from core.models import Login
from administracao.models import Tecnico
from equipamentos.models import Equipamento

class Agendamento(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_agendada = models.DateField()
    hora_inicio_agendamento = models.TimeField()
    hora_termino_agendamento = models.TimeField()
    data_solicitacao_agendamento = models.DateField()
    hora_solicitacao_agendamento = models.TimeField()
    additional_info = models.JSONField()
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, blank=False, null=False, related_name='login_tecnico')
