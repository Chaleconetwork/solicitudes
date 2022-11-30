# Generated by Django 4.1.1 on 2022-11-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_estadocivil_estadocivilid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadocivil',
            name='estadoCivil',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='estado_civil',
            field=models.ForeignKey(blank=True, choices=[('soltero', 'Soltero'), ('casado', 'Casado')], null=True, on_delete=django.db.models.deletion.CASCADE, to='App.estadocivil'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='tipo_solicitud',
            field=models.ForeignKey(blank=True, choices=[('soltero', 'Soltero'), ('casado', 'Casado')], null=True, on_delete=django.db.models.deletion.CASCADE, to='App.tiposolicitud'),
        ),
        migrations.AlterField(
            model_name='tiposolicitud',
            name='tipoSolicitud',
            field=models.CharField(max_length=20),
        ),
    ]
