# Generated by Django 4.2.5 on 2024-01-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0003_feriado_fimdesemana_calendario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feriado',
            name='data',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fimdesemana',
            name='data',
            field=models.IntegerField(),
        ),
    ]
