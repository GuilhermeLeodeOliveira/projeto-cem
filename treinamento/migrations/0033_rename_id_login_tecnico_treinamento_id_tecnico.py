# Generated by Django 4.2.5 on 2024-02-22 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinamento', '0032_rename_id_login_tecnico_prova_id_tecnico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treinamento',
            old_name='id_login_tecnico',
            new_name='id_tecnico',
        ),
    ]