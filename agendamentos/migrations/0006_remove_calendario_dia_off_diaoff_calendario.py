# Generated by Django 4.2.5 on 2024-01-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0005_rename_fimdesemana_diaoff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendario',
            name='dia_off',
        ),
        migrations.AddField(
            model_name='diaoff',
            name='calendario',
            field=models.ManyToManyField(blank=True, null=True, to='agendamentos.calendario'),
        ),
    ]