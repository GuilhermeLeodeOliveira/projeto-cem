# Generated by Django 4.2.5 on 2024-02-22 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinamento', '0031_prova'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prova',
            old_name='id_login_tecnico',
            new_name='id_tecnico',
        ),
    ]
