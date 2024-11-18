# Generated by Django 4.2.11 on 2024-11-18 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inf236backend', '0003_auto_20241117_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('antecedente_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_description', models.TextField(blank=True, default='', null=True)),
                ('antecedente_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Asign',
        ),
        migrations.RemoveField(
            model_name='incidencia',
            name='usuario',
        ),
        migrations.AddField(
            model_name='componente',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=256),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='camion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inf236backend.camion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidencia',
            name='descripcion_trabajo_hecho',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='mecanico_asignado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inf236backend.usuario'),
        ),
        migrations.AlterField(
            model_name='asignacionmotorcamion',
            name='fecha_asignacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='camion',
            name='durabilidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='camion',
            name='estado',
            field=models.CharField(default='Operativo', max_length=256),
        ),
        migrations.AlterField(
            model_name='camion',
            name='n_serie',
            field=models.CharField(default='XXX', max_length=256),
        ),
        migrations.AlterField(
            model_name='camion',
            name='placa',
            field=models.CharField(default='XXXXXX', max_length=6),
        ),
        migrations.AlterField(
            model_name='componente',
            name='durabilidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='componente',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='componente',
            name='n_serie',
            field=models.CharField(default='XXX', max_length=256),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='descripcion_problema',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='descripcion_trabajo_necesario',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='fecha_incidencia',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='mecanicos_asociados',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='motor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inf236backend.motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='durabilidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='motor',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='motor',
            name='n_serie',
            field=models.CharField(default='XXX', max_length=256),
        ),
        migrations.AlterField(
            model_name='motor',
            name='tiempo_en_uso',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sistema',
            name='n_serie',
            field=models.CharField(default='XXX', max_length=256),
        ),
        migrations.AlterField(
            model_name='sistema',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=256),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='Apellido', max_length=256),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(default='Contrasena', max_length=256),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=256),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='mecanico', max_length=256),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default='RUT', max_length=256),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='turno',
            field=models.CharField(default='4x7', max_length=256),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='camion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inf236backend.camion'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='motor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inf236backend.motor'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inf236backend.usuario'),
        ),
    ]
