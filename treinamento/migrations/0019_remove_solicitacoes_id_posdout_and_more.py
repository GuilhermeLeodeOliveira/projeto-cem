# Generated by Django 4.2.5 on 2023-12-06 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinamento', '0018_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacoes',
            name='id_PosDout',
        ),
        migrations.RemoveField(
            model_name='treinamento',
            name='id_PosDout',
        ),
    ]