# Generated by Django 4.2.5 on 2023-12-17 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0007_remove_precadtecnico_info_projeto_and_more'),
        ('treinamento', '0020_remove_solicitacoes_id_alunoposic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treinamento',
            name='id_tecnico',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='administracao.tecnico'),
        ),
    ]
