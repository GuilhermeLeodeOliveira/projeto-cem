from django.db import models
from administracao.models import Tecnico

# Create your models here.

class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=10)
    origem = models.CharField(max_length=10)
    ano_aquisicao = models.CharField(max_length=255)
    sala = models.CharField(max_length=20)
    divisao = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20)
    comentario = models.CharField(max_length=20)
    chave = models.CharField(max_length=255)
    patrimonio = models.CharField(max_length=255)
    aquisicao = models.CharField(max_length=100)
    prof = models.CharField(max_length=255)
    tecnicos = models.ManyToManyField(Tecnico)

    def __str__(self):
        return self.nome

