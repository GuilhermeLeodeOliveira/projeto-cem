# Generated by Django 4.2.5 on 2023-10-29 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0008_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipamento',
            name='id_tecnico',
        ),
    ]
