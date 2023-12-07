# Generated by Django 4.2.5 on 2023-12-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0017_alter_equipamento_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='ano_aquisicao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='aquisicao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='chave',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='comentario',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='divisao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='origem',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='patrimonio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='prof',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='sala',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
