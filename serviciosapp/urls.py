from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from serviciosapp import views

urlpatterns = [
    path('Servicios', views.Servicios, name="Servicios"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)