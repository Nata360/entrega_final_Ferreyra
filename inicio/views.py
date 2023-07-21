from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from inicio.models import *
from inicio.form import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')


class CrearBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'inicio/crear_blog.html'
    fields = ['nombre_blog', 'nombre_autor', 'apellido_autor', 'categoria', 'descripcion']
    success_url = reverse_lazy('inicio:inicio')
    
class ListaDeBlogs(ListView):
    model = Blog
    template_name = "inicio/lista_blogs.html"
    context_object_name = 'blogs'
    
    def get_queryset(self):
        listado_blogs = []
        formulario = BuscarBlogFormulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['nombre']
            listado_blogs = Blog.objects.filter(nombre_blog__icontains=nombre_a_buscar)
        return listado_blogs
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarBlogFormulario
        return contexto
        
    
class EditarBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'inicio/editar_blog.html'
    fields = ['nombre_blog', 'categoria', 'descripcion']
    success_url = reverse_lazy('inicio:lista_blogs')
    
class EliminarBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'inicio/eliminar_blog.html'
    success_url = reverse_lazy('inicio:lista_blogs')

class VerBlog(DetailView):
    model = Blog
    template_name = 'inicio/ver_blog.html'
    

@login_required
def subir_imagen(request):
    if request.method == 'POST':
        formulario = ImagenFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            nueva_imagen = Imagen(imagen= formulario.cleaned_data['imagen'], titulo = formulario.cleaned_data['titulo'], descripcion=formulario.cleaned_data['descripcion'], blog = formulario.cleaned_data['blog'])
            nueva_imagen.save()
            return render(request, 'inicio/subir_imagen.html', {'formulario':formulario})
        else:
            return render(request, 'inicio/subir_imagen.html', {'formulario':formulario})
    else:
        formulario = ImagenFormulario()
        return render(request, 'inicio/subir_imagen.html', {'formulario':formulario})

        
def imagen_galeria(request):
    imagenes = Imagen.objects.all()
    print(imagenes)
    return render(request, 'inicio/ver_blog.html', {'imagenes':imagenes})


# -----------RESGUARDO-----------
# def subir_imagen(request):
#     if request.method == 'POST':
#         formulario = ImagenFormulario(request.POST, request.FILES)
#         if formulario.is_valid():
            
#             # blog = formulario.cleaned_data.get('blog')
#             # Imagen.objects.get_or_create(blog=)
            
#             nueva_imagen = Imagen(imagen = formulario.cleaned_data['imagen'], titulo = formulario.cleaned_data['titulo'])
#             nueva_imagen.save()
            
#         return render(request, 'galeria/subir_imagen.html', {'formulario':formulario})
#     else:
#         formulario = ImagenFormulario()
            
#     return render(request, 'galeria/subir_imagen.html', {'formulario':formulario}) 

# def eliminar_imagen(request, imagen_id):
#     imagen = Imagen.objects.get(id=imagen_id)
#     imagen.delete()
    
#     return redirect('galeria:albun')
       
