from django.db import models
from datetime import datetime

# Create your models here.

class EstadoCivil(models.Model):

    estadoCivilId = models.AutoField(primary_key = True)
    estadoCivil = models.CharField(max_length = 20)

    def estadosCiviles(self):
        return "{}".format(self.estadoCivil)

    def __str__(self):
        return self.estadosCiviles()

class TipoSolicitud(models.Model):

    tipoSolicitudId = models.AutoField(primary_key = True)
    tipoSolicitud = models.CharField(max_length = 20)

    def tiposSolicitudes(self):
        return "{}".format(self.tipoSolicitud)

    def __str__(self):
        return self.tiposSolicitudes()

class Solicitud(models.Model):

    id_solicitud = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length = 20)
    apPaterno = models.CharField(max_length = 20, verbose_name = 'Apellido Paterno')
    apMaterno = models.CharField(max_length = 20, verbose_name = 'Apellido Materno')
    rut = models.IntegerField()
    dv = models.CharField(max_length = 20)
    fnacimiento = models.DateField(verbose_name = 'Fecha de nacimiento')
    donante = models.CharField(max_length = 20)
    fsolicitud = models.DateField(default=datetime.now, blank=True, verbose_name = 'Fecha de Solicitud')
    observaciones = models.TextField(max_length = 50)

    estadoCivilId = models.ForeignKey(EstadoCivil, null = True, blank = True, verbose_name = 'Estado Civil', on_delete = models.CASCADE)
    tipoSolicitudId = models.ForeignKey(TipoSolicitud, null = True, blank = True, verbose_name = 'Tipo de Solicitud', on_delete = models.CASCADE)