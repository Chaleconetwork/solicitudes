# Generated by Django 4.1.1 on 2022-11-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_solicitud_apmaterno_alter_solicitud_appaterno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='observaciones',
            field=models.TextField(max_length=50),
        ),
    ]