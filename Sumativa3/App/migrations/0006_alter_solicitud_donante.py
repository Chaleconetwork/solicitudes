# Generated by Django 4.1.1 on 2022-11-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_solicitud_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='donante',
            field=models.CharField(max_length=20),
        ),
    ]
