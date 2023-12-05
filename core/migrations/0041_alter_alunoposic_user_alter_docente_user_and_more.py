# Generated by Django 4.2.5 on 2023-12-04 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_alunoposic_user_alter_docente_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunoposic',
            name='user',
            field=models.OneToOneField(default='3', on_delete=django.db.models.deletion.CASCADE, to='core.login'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='core.login'),
        ),
        migrations.AlterField(
            model_name='userexterno',
            name='user',
            field=models.OneToOneField(default='3', on_delete=django.db.models.deletion.CASCADE, to='core.login'),
        ),
    ]
