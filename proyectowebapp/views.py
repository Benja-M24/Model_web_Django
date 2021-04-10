from django.shortcuts import render, HttpResponse

def Home(request):
    return render(request, 'proyectowebapp/home.html')

def Tienda(request):
    return render(request, 'proyectowebapp/tienda.html')

def Contacto(request):
    return render(request, 'proyectowebapp/contacto.html')
