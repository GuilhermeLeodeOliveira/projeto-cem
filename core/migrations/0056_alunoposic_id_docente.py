# Generated by Django 4.2.5 on 2023-12-04 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_remove_alunoposic_email_inst_remove_alunoposic_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunoposic',
            name='id_docente',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.docente'),
        ),
    ]
