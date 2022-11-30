# Generated by Django 4.1.3 on 2022-11-30 22:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_remove_solicitud_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='apMaterno',
            field=models.CharField(max_length=20, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='apPaterno',
            field=models.CharField(max_length=20, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='estadoCivilId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.estadocivil', verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fnacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fsolicitud',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Fecha de Solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='tipoSolicitudId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.tiposolicitud', verbose_name='Tipo de Solicitud'),
        ),
    ]
