# Generated by Django 4.2.5 on 2023-12-03 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinamento', '0014_treinamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacoes',
            name='id_AlunoPosIC',
        ),
        migrations.RemoveField(
            model_name='treinamento',
            name='id_AlunoPosIC',
        ),
    ]
