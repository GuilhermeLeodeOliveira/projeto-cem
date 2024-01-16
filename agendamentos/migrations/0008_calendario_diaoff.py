# Generated by Django 4.2.5 on 2024-01-16 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0007_remove_diaoff_calendario_delete_calendario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id_calendario', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('quantidade_dias', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DiaOff',
            fields=[
                ('id_dia_off', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.IntegerField()),
                ('calendario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.calendario')),
            ],
        ),
    ]
