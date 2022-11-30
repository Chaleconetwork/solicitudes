from django.shortcuts import render, redirect
from .forms import FormSolicitud
from .models import Solicitud
from .filters import MainFilter
import datetime

# Create your views here.

def home(request):
    return render(request, 'index.html')

def createRequest(request):
    frm = FormSolicitud()

    field = frm.fields['fsolicitud']
    field.widget = field.hidden_widget()

    if (request.method == 'POST'):
        frm = FormSolicitud(request.POST)
        if (frm.is_valid()):            
            print("Solicitud registrada")
            frm.save()
            return redirect('createRequest')
        else:
            print("Error")
    
    data = {'frm': frm, 'titulo': 'Realizar solicitud'}

    return render(request, 'createRequest.html', data)

def requestList(request):

    currentYear = datetime.date.today().year

    solicitudes = Solicitud.objects.filter(fsolicitud=datetime.date.today())
    # solicitudes = Solicitud.objects.all()

    myFilter = MainFilter(request.GET, queryset=solicitudes)
    solicitudes = myFilter.qs

    for i in solicitudes:
        i.fnacimiento = currentYear - i.fnacimiento.year

    data = {'solicitudes': solicitudes, 'myFilter': myFilter}
    
    return render(request, 'requestslist.html', data)

def deleteRequest(request, id):
    solicitudes = Solicitud.objects.get(id_solicitud = id)
    solicitudes.delete()
    return redirect('requestList')