# Generated by Django 4.2.5 on 2023-12-11 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0006_alter_tecnico_celular_alter_tecnico_centro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precadtecnico',
            name='info_projeto',
        ),
        migrations.RemoveField(
            model_name='precadtecnico',
            name='lista_publi',
        ),
        migrations.RemoveField(
            model_name='precadtecnico',
            name='possui_projeto',
        ),
        migrations.RemoveField(
            model_name='precadtecnico',
            name='programa_pos',
        ),
        migrations.RemoveField(
            model_name='tecnico',
            name='info_projeto',
        ),
        migrations.RemoveField(
            model_name='tecnico',
            name='lista_publi',
        ),
        migrations.RemoveField(
            model_name='tecnico',
            name='possui_projeto',
        ),
    ]
