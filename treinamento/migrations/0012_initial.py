# Generated by Django 4.2.5 on 2023-11-17 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0029_remove_alunoposic_id_form_infra_and_more'),
        ('equipamentos', '0015_initial'),
        ('treinamento', '0011_remove_treinamento_id_alunoposic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacoes',
            fields=[
                ('id_solicitacao', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('status', models.CharField(max_length=50)),
                ('id_AlunoPosIC', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.alunoposic')),
                ('id_Docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.docente')),
                ('id_PosDout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.posdout')),
                ('id_UserExterno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.userexterno')),
                ('id_equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.equipamento')),
            ],
        ),
        migrations.CreateModel(
            name='Treinamento',
            fields=[
                ('id_terinamento', models.AutoField(primary_key=True, serialize=False)),
                ('data_treinamento', models.DateField()),
                ('hora_inicio_treinamento', models.TimeField()),
                ('hora_termino_treinamento', models.TimeField()),
                ('local_treinamento', models.CharField(max_length=50)),
                ('compareceu', models.CharField(blank=True, max_length=5, null=True)),
                ('justificativa', models.CharField(blank=True, max_length=225, null=True)),
                ('aptidao', models.CharField(max_length=10)),
                ('id_AlunoPosIC', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.alunoposic')),
                ('id_Docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.docente')),
                ('id_PosDout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.posdout')),
                ('id_UserExterno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.userexterno')),
                ('id_equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.equipamento')),
                ('id_solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinamento.solicitacoes')),
            ],
        ),
    ]