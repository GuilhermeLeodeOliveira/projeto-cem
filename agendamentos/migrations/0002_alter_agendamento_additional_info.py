# Generated by Django 4.2.5 on 2024-01-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='additional_info',
            field=models.JSONField(),
        ),
    ]