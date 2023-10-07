from django.db import models

# Create your models here.

class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    prof = models.CharField(max_length=255)

 #   def __str__(self):
  #      return f"{self.nome} {self.provider} {self.contato} {self.tipo} {self.status} {self.comentario} {self.descricao} {self.prof}"