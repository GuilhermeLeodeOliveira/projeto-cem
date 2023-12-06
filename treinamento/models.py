from django.db import models
from core.models import Docente, AlunoPosIC, UserExterno
from equipamentos.models import Equipamento
# Create your models here.

class Solicitacoes(models.Model):
    id_solicitacao = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=50)
    id_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, null=True)
    id_AlunoPosIC = models.ForeignKey(AlunoPosIC, on_delete=models.CASCADE, blank=True, null=True)
    id_UserExterno = models.ForeignKey(UserExterno, on_delete=models.CASCADE, blank=True, null=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    

class Treinamento(models.Model):
    id_treinamento = models.AutoField(primary_key=True)
    data_treinamento = models.DateField()
    hora_inicio_treinamento = models.TimeField()
    hora_termino_treinamento = models.TimeField()
    local_treinamento = models.CharField(max_length=50)
    compareceu = models.CharField(max_length=5, blank=True, null=True)
    justificativa = models.CharField(max_length=225, blank=True, null=True)
    aptidao = models.CharField(max_length=10)
    id_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, null=True)
    id_AlunoPosIC = models.ForeignKey(AlunoPosIC, on_delete=models.CASCADE, blank=True, null=True)
    id_UserExterno = models.ForeignKey(UserExterno, on_delete=models.CASCADE, blank=True, null=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    id_solicitacao = models.ForeignKey(Solicitacoes, on_delete=models.CASCADE, blank=False, null=False)
