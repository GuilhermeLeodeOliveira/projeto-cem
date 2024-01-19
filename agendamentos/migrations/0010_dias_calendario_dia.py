# Generated by Django 4.2.5 on 2024-01-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0009_remove_diaoff_calendario_calendario_dia_off'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id_dia', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='calendario',
            name='dia',
            field=models.ManyToManyField(blank=True, null=True, to='agendamentos.dias'),
        ),
    ]
