# Generated by Django 4.2.5 on 2024-01-29 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0016_mes_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mes',
            name='numero',
            field=models.TextField(default=0),
        ),
    ]