# Generated by Django 4.2.5 on 2023-10-27 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipamentos', '0004_delete_equipamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id_equipamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=20)),
                ('fabricante', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=100)),
                ('origem', models.CharField(max_length=10)),
                ('ano_aquisicao', models.CharField(max_length=4)),
                ('contato', models.CharField(max_length=255)),
                ('sala', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255)),
                ('manutencao', models.CharField(max_length=20)),
                ('comentario', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('coordenacao', models.CharField(max_length=100)),
                ('prof', models.CharField(max_length=255)),
                ('tecnico', models.CharField(max_length=100)),
            ],
        ),
    ]