from django.db import models

# Create your models here.

class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    provider = models.TextField(max_length=255)
    contato = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255, null=True)
    status = models.TextField(max_length=255)
    comentario = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    prof = models.TextField(max_length=255)

    def __str__(self):
        return self.nome