# Generated by Django 4.2.5 on 2023-12-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0016_alter_equipamento_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='localizacao',
            field=models.CharField(max_length=30),
        ),
    ]
