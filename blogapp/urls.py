from django.urls import path
from blogapp import views

urlpatterns = [
    path('Blog', views.Blog, name="Blog"),
    path('Categoria/<int:categoria_id>', views.Catg, name="Categoria" )
]