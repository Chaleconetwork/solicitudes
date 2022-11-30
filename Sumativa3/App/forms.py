from django import forms
from .choices import donar
from django.forms.widgets import DateTimeInput
import datetime

from .models import Solicitud

class FormSolicitud(forms.ModelForm):

    donante = forms.ChoiceField(choices=donar, widget=forms.RadioSelect)
    donante.widget.attrs['class']='radios'
    fsolicitud = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'fnacimiento': DateTimeInput( attrs={'type': 'date'})
        }
        