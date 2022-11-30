from django.contrib import admin
from .models import Solicitud, TipoSolicitud, EstadoCivil

# Register your models here.

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id_solicitud', 'nombres', 'estadoCivilId')


@admin.register(EstadoCivil)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('estadoCivilId', 'estadoCivil')

# admin.site.register(Solicitud)
admin.site.register(TipoSolicitud)
# admin.site.register(EstadoCivil)
