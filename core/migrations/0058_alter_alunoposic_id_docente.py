# Generated by Django 4.2.5 on 2023-12-04 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_alter_alunoposic_id_docente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunoposic',
            name='id_docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.docente'),
        ),
    ]
