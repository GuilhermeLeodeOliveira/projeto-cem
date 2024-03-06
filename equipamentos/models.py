from django.db import models
from administracao.models import Tecnico

# Create your models here.

class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=30)
    origem = models.CharField(max_length=10, blank=True, null=True)
    ano_aquisicao = models.CharField(max_length=255, blank=True, null=True)
    sala = models.CharField(max_length=20, blank=True, null=True)
    divisao = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    comentario = models.CharField(max_length=20, blank=True, null=True)
    chave = models.CharField(max_length=255, blank=True, null=True)
    patrimonio = models.CharField(max_length=255, blank=True, null=True)
    aquisicao = models.CharField(max_length=100, blank=True, null=True)
    tem_palestra = models.BooleanField(default=False)
    tem_prova = models.BooleanField(default=False)
    prof = models.CharField(max_length=255, blank=True, null=True)
    tecnicos = models.ManyToManyField(Tecnico, blank=True, null=True)

    def __str__(self):
        return self.nome

