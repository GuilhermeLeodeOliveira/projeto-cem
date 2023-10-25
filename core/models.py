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
    
class FormInfra(models.Model):
    id_form_infra = models.AutoField(primary_key=True)
    cem_sbc_equip = models.CharField(max_length=255)
    cem_sbc_equip_apoio = models.CharField(max_length=255)
    cem_sa_equip = models.CharField(max_length=255)

class FormTermo(models.Model):
    id_form_termo = models.AutoField(primary_key=True)
    veracidade1 = models.CharField(max_length=3)
    veracidade2 = models.CharField(max_length=3)
    veracidade3 = models.CharField(max_length=3)

class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255, unique=True)
    matricula_siape = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    centro = models.CharField(max_length=10)
    programa_pos = models.CharField(max_length=255)
    possui_projeto = models.CharField(max_length=3)
    info_projeto = models.TextField(max_length=255)
    lista_publi = models.TextField(max_length=255)
    id_form_infra = models.ForeignKey(FormInfra, on_delete=models.CASCADE, null=True)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome
    
    

class preCadDocente(models.Model):
    id_pre_cad_docente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255)
    matricula_siape = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    centro = models.CharField(max_length=10)
    programa_pos = models.CharField(max_length=255)
    possui_projeto = models.CharField(max_length=3)
    info_projeto = models.TextField(max_length=255)
    lista_publi = models.TextField(max_length=255)
    
    def __str__(self):
        return self.nome
    

class PosDout(models.Model):
    id_pos_dout = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255, unique=True)
    matricula_ufabc = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    nome_supervisor = models.CharField(max_length=255)
    centro = models.CharField(max_length=10)
    data_pos = models.DateField()
    possui_bolsa = models.CharField(max_length=10)
    programa_pos = models.TextField(max_length=255)
    plano_trabalho = models.TextField(max_length=255)
    declaracao_ciencia_supervisor = models.CharField(max_length=3)
    id_form_infra = models.ForeignKey(FormInfra, on_delete=models.CASCADE)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class preCadPosDout(models.Model):
    id_pre_cad_pos_dout = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255)
    matricula_ufabc = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    nome_supervisor = models.CharField(max_length=255)
    centro = models.CharField(max_length=10)
    data_pos = models.DateField()
    possui_bolsa = models.CharField(max_length=10)
    programa_pos = models.TextField(max_length=255)
    plano_trabalho = models.TextField(max_length=255)
    declaracao_ciencia_supervisor = models.CharField(max_length=3)
    

class AlunoPosIC(models.Model):
    id_aluno_pos_ic = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=255, unique=True)
    matricula_ufabc = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    nome_orientador = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    centro = models.CharField(max_length=10)
    data_pos = models.DateField()
    possui_bolsa = models.CharField(max_length=10)
    programa_pos = models.TextField(max_length=255)
    plano_trabalho = models.TextField(max_length=255)
    declaracao_ciencia_orientador = models.CharField(max_length=3)
    id_form_infra = models.ForeignKey(FormInfra, on_delete=models.CASCADE)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class preCadAlunoPosIC(models.Model):
    id_pre_cad_aluno_pos_ic = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=17, default=None)
    email_inst = models.EmailField(max_length=255)
    matricula_ufabc = models.CharField(max_length=10)
    ramal_lab = models.CharField(max_length=10)
    nome_orientador = models.CharField(max_length=255)
    departamento = models.TextField(max_length=255)
    centro = models.CharField(max_length=10)
    data_pos = models.DateField()
    possui_bolsa = models.CharField(max_length=10)
    programa_pos = models.TextField(max_length=255)
    plano_trabalho = models.TextField(max_length=255)
    declaracao_ciencia_orientador = models.CharField(max_length=3)

class preCadUserExterno(models.Model):
    id_pre_cad_user_externo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    atividade = models.CharField(max_length=150)
    endereco_inst = models.CharField(max_length=150)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=200)
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

class UserExterno(models.Model):
    id_user_externo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    atividade = models.CharField(max_length=150)
    endereco_inst = models.CharField(max_length=150)
    celular = models.CharField(max_length=17)
    email_inst = models.EmailField(max_length=200, unique=True)
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
    id_form_infra = models.ForeignKey(FormInfra, on_delete=models.CASCADE)
    id_form_termo = models.ForeignKey(FormTermo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    