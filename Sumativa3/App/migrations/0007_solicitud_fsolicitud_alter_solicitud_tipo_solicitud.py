# Generated by Django 4.1.1 on 2022-11-24 22:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_solicitud_donante'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='fsolicitud',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='tipo_solicitud',
            field=models.ForeignKey(blank=True, choices=[('consulta', 'Consulta'), ('dentista', 'Dentista')], null=True, on_delete=django.db.models.deletion.CASCADE, to='App.tiposolicitud'),
        ),
    ]
