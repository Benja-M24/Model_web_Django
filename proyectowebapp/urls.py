from django.urls import path
from proyectowebapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Tienda', views.Tienda, name="Tienda"),
    path('Contacto', views.Contacto, name="Contacto"),
]