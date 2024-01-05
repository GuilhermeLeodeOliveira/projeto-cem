from django.db import models
import datetime
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

class FormTermo(models.Model):
    id_form_termo = models.AutoField(primary_key=True)
    veracidade1 = models.CharField(max_length=3)
    veracidade2 = models.CharField(max_length=3)
    veracidade3 = models.CharField(max_length=3)

class preLogin(models.Model):
    id_pre_login = models.AutoField(primary_key=True)
    email_inst = models.EmailField(max_length=255)
    senha = models.CharField(max_length=50)
    perfil = models.CharField(max_length=30, default='perfil')
    password_change_required = models.BooleanField(default=True)

class Login(models.Model):
    id_login = models.AutoField(primary_key=True)
    email_inst = models.EmailField(max_length=255)
    senha = models.CharField(max_length=255)
    perfil = models.CharField(max_length=30, default='perfil')
    data_cadastro = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    data_ultimo_login = models.DateTimeField(blank=True, null=True, default=datetime.datetime(2023, 1, 1, 0, 0))
    password_change_required = models.BooleanField(default=True)

class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    matricula_siape = models.CharField(max_length=30)
    ramal_lab = models.CharField(max_length=30)
    centro = models.CharField(max_length=30)
    possui_projeto = models.CharField(max_length=3)
    info_projeto = models.TextField(max_length=255)
    lista_publi = models.TextField(max_length=255)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE, null=False)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, null=False, default=0)

    def __str__(self):
        return self.primeiro_nome
    

class preCadDocente(models.Model):
    id_pre_cad_docente = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255)
    senha = models.CharField(max_length=50)
    matricula_siape = models.CharField(max_length=30)
    ramal_lab = models.CharField(max_length=30)
    centro = models.CharField(max_length=30)
    programa_pos = models.CharField(max_length=255)
    possui_projeto = models.CharField(max_length=3)
    info_projeto = models.TextField(max_length=255)
    lista_publi = models.TextField(max_length=255)
    id_login = models.ForeignKey(preLogin, on_delete=models.CASCADE, null=False, default=0)
    
    def __str__(self):
        return self.email_inst


class AlunoPosIC(models.Model):
    id_aluno_pos_ic = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    matricula_ufabc = models.CharField(max_length=30)
    ramal_lab = models.CharField(max_length=30)
    nome_orientador = models.CharField(max_length=255)
    perfil = models.CharField(max_length=30)
    data_pos = models.DateField()
    centro = models.CharField(max_length=30)
    bolsa = models.CharField(max_length=30)
    plano_trabalho = models.TextField()
    declaracao_ciencia_orientador = models.CharField(max_length=3)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE, null=False)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, null=False, default=0)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.primeiro_nome


class preCadAlunoPosIC(models.Model):
    id_pre_cad_aluno_pos_ic = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255)
    senha = models.CharField(max_length=50)
    matricula_ufabc = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    nome_orientador = models.CharField(max_length=255)
    perfil = models.CharField(max_length=30)
    data_pos = models.DateField()
    centro = models.CharField(max_length=10)
    bolsa = models.CharField(max_length=10)
    plano_trabalho = models.TextField()
    declaracao_ciencia_orientador = models.CharField(max_length=3)
    id_login = models.ForeignKey(preLogin, on_delete=models.CASCADE, null=False, default=0)

class UserExterno(models.Model):
    id_user_externo = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=100)
    atividade = models.CharField(max_length=150)
    endereco_inst = models.CharField(max_length=150)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=200, unique=True)
    senha = models.CharField(max_length=50)
    telefone_sala = models.CharField(max_length=200)
    formacao = models.CharField(max_length=200)
    classificacao = models.CharField(max_length=100)
    nome_centro_docente = models.CharField(max_length=150)
    possui_projeto = models.CharField(max_length=3)
    arquivo = models.FileField(upload_to='uploads/')
    infos_projeto = models.TextField(max_length=200)
    publicacoes = models.TextField(max_length=255)
    plano_trabalho = models.TextField(max_length=255)
    manifesto_apoio = models.CharField(max_length=3)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE, null=False)
    id_login = models.ForeignKey(Login, on_delete=models.CASCADE, null=False, default=0)

    def __str__(self):
        return self.email_inst
    
class preCadUserExterno(models.Model):
    id_pre_cad_user_externo = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=255)
    segundo_nome = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=100)
    atividade = models.CharField(max_length=150)
    endereco_inst = models.CharField(max_length=150)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=200)
    senha = models.CharField(max_length=50)
    telefone_sala = models.CharField(max_length=200)
    formacao = models.CharField(max_length=200)
    classificacao = models.CharField(max_length=100)
    nome_centro_docente = models.CharField(max_length=150)
    possui_projeto = models.CharField(max_length=3)
    arquivo = models.FileField(upload_to='uploads/')
    infos_projeto = models.TextField(max_length=200)
    publicacoes = models.TextField(max_length=255)
    plano_trabalho = models.TextField(max_length=255)
    manifesto_apoio = models.CharField(max_length=3)
    id_login = models.ForeignKey(preLogin, on_delete=models.CASCADE, null=False, default=0)