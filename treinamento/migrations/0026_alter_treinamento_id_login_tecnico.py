# Generated by Django 4.2.5 on 2023-12-17 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_alter_alunoposic_bolsa_alter_alunoposic_centro_and_more'),
        ('treinamento', '0025_alter_treinamento_id_login_tecnico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treinamento',
            name='id_login_tecnico',
            field=models.ForeignKey(default='teste', on_delete=django.db.models.deletion.CASCADE, related_name='login_tecnico', to='core.login'),
        ),
    ]
