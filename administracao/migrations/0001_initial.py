# Generated by Django 4.2.5 on 2023-10-27 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adm',
            fields=[
                ('id_adm', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]