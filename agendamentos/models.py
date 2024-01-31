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
    additional_info = models.TextField()
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, blank=False, null=False, related_name='login_tecnico')


class Mes(models.Model):
    id_mes = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    numero = models.CharField(max_length=2, default = 0)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome

class Dia(models.Model):
    id_dia = models.AutoField(primary_key=True)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    numero = models.CharField(max_length=2, default = 0)
    dia_da_semana = models.CharField(max_length=20)  # Pode ser 'segunda', 'terca', etc.
    feriado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero} - {self.dia_da_semana} ({'Feriado' if self.feriado else 'Dia útil'}) de {self.mes}"