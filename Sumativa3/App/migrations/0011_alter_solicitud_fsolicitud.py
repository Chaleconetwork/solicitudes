# Generated by Django 4.1.1 on 2022-11-25 21:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_alter_solicitud_fsolicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fsolicitud',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
