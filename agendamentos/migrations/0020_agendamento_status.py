# Generated by Django 4.2.5 on 2024-03-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0019_alter_dia_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='status',
            field=models.TextField(null=True),
        ),
    ]
