# Generated by Django 4.2.5 on 2024-01-23 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0014_mes_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='additional_info',
            field=models.TextField(),
        ),
    ]