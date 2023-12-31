# Generated by Django 4.2.5 on 2023-10-06 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0002_equipamento_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='comentario',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='contato',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='prof',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='provider',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='tipo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
