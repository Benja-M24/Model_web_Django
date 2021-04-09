from django.shortcuts import render
from serviciosapp.models import Servicio
# def Ejemplo(request):
#     return HttpResponse("Vista de ejemplo")

def Servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'serviciosapp/servicios.html', {'servicios': servicios})
