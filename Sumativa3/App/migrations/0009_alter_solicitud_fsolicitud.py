# Generated by Django 4.1.1 on 2022-11-24 23:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_solicitud_fsolicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fsolicitud',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
