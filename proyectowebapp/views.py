from django.shortcuts import render, HttpResponse

def Home(request):
    return render(request, 'proyectowebapp/home.html')

def Tienda(request):
    return render(request, 'proyectowebapp/tienda.html')

def Blog(request):
    return render(request, 'proyectowebapp/blog.html')

def Contacto(request):
    return render(request, 'proyectowebapp/contacto.html')
