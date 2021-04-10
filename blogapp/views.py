from django.shortcuts import render
from .models import Post, Categoria
from blogapp import models

def Blog(request):
    post = Post.objects.all()
    return render(request, 'blogapp/blog.html', {'post': post})

def Catg(request, categoria_id):
    categ = Categoria,object.get(id=categoria_id)
    post = Post.objects.filter(Categorias = categ)
    return render(request, 'blogapp/Categoria.html', {'categoria': categ, 'post': post})

