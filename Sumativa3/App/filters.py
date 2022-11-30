import django_filters as Filter

from .models import Solicitud

class MainFilter(Filter.FilterSet):

    class Meta:
        model = Solicitud
        fields = ['fsolicitud', 'fnacimiento', 'donante', 'estadoCivilId', 'tipoSolicitudId']
