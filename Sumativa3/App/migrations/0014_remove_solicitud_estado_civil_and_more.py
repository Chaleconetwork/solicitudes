# Generated by Django 4.1.1 on 2022-11-26 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_alter_solicitud_estado_civil_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='estado_civil',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='tipo_solicitud',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estadoCivilId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.estadocivil'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipoSolicitudId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.tiposolicitud'),
        ),
    ]
