# Generated by Django 4.2.5 on 2023-12-21 03:11

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0062_alter_alunoposic_bolsa_alter_alunoposic_centro_and_more'),
        ('equipamentos', '0019_alter_equipamento_tecnicos'),
    ]

    operations = [
        migrations.CreateModel(
            name='agendamento',
            fields=[
                ('id_agendamento', models.AutoField(primary_key=True, serialize=False)),
                ('data_agendada', models.DateField()),
                ('hora_inicio_agendamento', models.TimeField()),
                ('hora_termino_agendamento', models.TimeField()),
                ('data_solicitacao_agendamento', models.DateField()),
                ('hora_solicitacao_agendamento', models.TimeField()),
                ('additional_info', jsonfield.fields.JSONField()),
                ('id_equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.equipamento')),
                ('id_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_tecnico', to='core.login')),
            ],
        ),
    ]
