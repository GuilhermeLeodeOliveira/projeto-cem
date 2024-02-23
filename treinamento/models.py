from django.db import models
from core.models import Login
from administracao.models import Tecnico
from equipamentos.models import Equipamento
# Create your models here.

class Solicitacoes(models.Model):
    id_solicitacao = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=50)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, blank=True, null=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    
class Prova(models.Model):
    id_prova = models.AutoField(primary_key=True)
    data_prova = models.DateField()
    hora_inicio_prova = models.TimeField()
    hora_termino_prova = models.TimeField()
    local_prova = models.CharField(max_length=50)
    compareceu = models.CharField(max_length=5, blank=True, null=True)
    justificativa = models.CharField(max_length=225, blank=True, null=True)
    aptidao = models.CharField(max_length=10, blank=True, null=True)  
    id_login_usuario = models.ForeignKey(Login, on_delete=models.CASCADE, blank=True, null=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, blank=False, null=False)
    id_solicitacao = models.ForeignKey(Solicitacoes, on_delete=models.CASCADE, blank=False, null=False)

class Treinamento(models.Model):
    id_treinamento = models.AutoField(primary_key=True)
    data_treinamento = models.DateField()
    hora_inicio_treinamento = models.TimeField()
    hora_termino_treinamento = models.TimeField()
    local_treinamento = models.CharField(max_length=50)
    compareceu = models.CharField(max_length=5, blank=True, null=True)
    justificativa = models.CharField(max_length=225, blank=True, null=True)
    aptidao = models.CharField(max_length=10)  
    id_login_usuario = models.ForeignKey(Login, on_delete=models.CASCADE, blank=True, null=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, blank=False, null=False)
    id_solicitacao = models.ForeignKey(Solicitacoes, on_delete=models.CASCADE, blank=False, null=False)

