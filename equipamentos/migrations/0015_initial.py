# Generated by Django 4.2.5 on 2023-11-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracao', '0004_tecnico'),
        ('equipamentos', '0014_delete_equipamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id_equipamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=10)),
                ('origem', models.CharField(max_length=10)),
                ('ano_aquisicao', models.CharField(max_length=255)),
                ('sala', models.CharField(max_length=20)),
                ('divisao', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=20)),
                ('comentario', models.CharField(max_length=20)),
                ('chave', models.CharField(max_length=255)),
                ('patrimonio', models.CharField(max_length=255)),
                ('aquisicao', models.CharField(max_length=100)),
                ('prof', models.CharField(max_length=255)),
                ('tecnicos', models.ManyToManyField(to='administracao.tecnico')),
            ],
        ),
    ]
