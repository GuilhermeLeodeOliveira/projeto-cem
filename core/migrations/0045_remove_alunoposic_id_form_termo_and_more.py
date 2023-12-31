# Generated by Django 4.2.5 on 2023-12-04 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinamento', '0017_remove_treinamento_id_alunoposic_and_more'),
        ('core', '0044_remove_alunoposic_user_remove_docente_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunoposic',
            name='id_form_termo',
        ),
        migrations.RemoveField(
            model_name='docente',
            name='id_form_termo',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.RemoveField(
            model_name='posdout',
            name='id_form_termo',
        ),
        migrations.DeleteModel(
            name='preCadAlunoPosIC',
        ),
        migrations.DeleteModel(
            name='preCadDocente',
        ),
        migrations.DeleteModel(
            name='preCadPosDout',
        ),
        migrations.DeleteModel(
            name='preCadUserExterno',
        ),
        migrations.DeleteModel(
            name='ProgramaPosGraduacao',
        ),
        migrations.RemoveField(
            model_name='userexterno',
            name='id_form_termo',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='AlunoPosIC',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='FormTermo',
        ),
        migrations.DeleteModel(
            name='PosDout',
        ),
        migrations.DeleteModel(
            name='UserExterno',
        ),
    ]
