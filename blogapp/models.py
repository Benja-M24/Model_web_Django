from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="Categoria"
        verbose_name_plural ="Categorias"

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to = 'blogapp', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categoria=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="Post"
        verbose_name_plural ="Posts"

    def __str__(self):
        return self.titulo
