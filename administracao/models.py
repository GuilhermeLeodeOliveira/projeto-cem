from django.db import models

# Create your models here.
class Adm(models.Model):
    id_adm = models.AutoField(primary_key=True)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
    divisao = models.CharField(max_length=50)

    def __str__(self):  
        return self.nome