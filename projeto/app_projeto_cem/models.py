from django.db import models



#Parte de Banco de dados, aqui consigo criar tabelas por codigos python e o django traduz em sql

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()


