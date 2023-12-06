from django.db import models
from core.models import FormTermo, Login, preLogin
# Create your models here.
class Adm(models.Model):
    id_adm = models.AutoField(primary_key=True)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    matricula_siape = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    centro = models.CharField(max_length=10)
    possui_projeto = models.CharField(max_length=3)
    info_projeto = models.TextField(max_length=255)
    lista_publi = models.TextField(max_length=255)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE, null=False)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, null=False, default=0)

    def __str__(self):  
        return self.nome
    
class preCadTecnico(models.Model):
    id_pre_cad_tecnico = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255)
    senha = models.CharField(max_length=50)
    matricula_siape = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    centro = models.CharField(max_length=10)
    programa_pos = models.CharField(max_length=255)
    possui_projeto = models.CharField(max_length=3)
    info_projeto = models.TextField(max_length=255)
    lista_publi = models.TextField(max_length=255)
    id_login = models.ForeignKey(preLogin, on_delete=models.CASCADE, null=False, default=0)