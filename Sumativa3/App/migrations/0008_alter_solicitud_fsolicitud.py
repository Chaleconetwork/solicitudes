# Generated by Django 4.1.1 on 2022-11-24 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_solicitud_fsolicitud_alter_solicitud_tipo_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fsolicitud',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
