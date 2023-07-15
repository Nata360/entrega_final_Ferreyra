from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from inicio.models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')

def sin_datos(request):
    return render(request, 'inicio/no_datos.html')

class CrearBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'inicio/crear_blog.html'
    fields = ['nombre_blog', 'nombre_autor', 'apellido_autor', 'categoria', 'descripcion']
    success_url = reverse_lazy('inicio:inicio')
    
class ListaDeBlogs(ListView):
    model = Blog
    template_name = "inicio/lista_blogs.html"
    context_object_name = 'blogs'
    
