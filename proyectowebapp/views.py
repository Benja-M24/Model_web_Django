from django.shortcuts import render, HttpResponse

def Home(request):
    return HttpResponse("Inicio")

def Servicios(request):
    return HttpResponse("Servicios")

def Tienda(request):
    return HttpResponse("Tienda")

def Blog(request):
    return HttpResponse("Blog")

def Contacto(request):
    return HttpResponse("Contacto")
