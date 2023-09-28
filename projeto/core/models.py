from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    
    def __str__(self):
        return self.nome
    

class ProgramaPosGraduacao(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nome_programa = models.TextField(max_length=255)

    def __str__(self):
        return self.nome_programa