# Generated by Django 4.2.5 on 2024-01-29 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0017_alter_mes_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mes',
            name='numero',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
