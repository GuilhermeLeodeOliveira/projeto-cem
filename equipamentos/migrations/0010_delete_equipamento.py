# Generated by Django 4.2.5 on 2023-10-29 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0009_remove_equipamento_id_tecnico'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Equipamento',
        ),
    ]
