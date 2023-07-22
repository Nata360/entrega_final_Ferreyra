from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
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
    fields = ['nombre_blog', 'nombre_autor', 'apellido_autor', 'categoria', 'descripcion',]
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
    context_object_name = 'blog'

class CrearAlbun(LoginRequiredMixin,CreateView):
    model = Albun
    form_class = CrearAlbunFormulario
    template_name = 'inicio/crear_albun.html'
    success_url = reverse_lazy('inicio:lista_albun')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            blog = None
        context['blog'] = blog
        return context
       
    def form_valid(self, form):
        blog = self.get_context_data().get('blog')
        if blog:
            form.instance.blog = blog
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        

class ListaAlbun(ListView):
    model = Albun
    template_name = 'inicio/lista_albun.html'
    context_object_name = 'albunes'
    
class VerAlbun(DetailView):
    model = Albun
    template_name = 'inicio/ver_albun.html'
    context_object_name = 'albun'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albun = self.get_object()
        imagenes = Imagen.objects.filter(albun=albun)
        context['albun_data'] = [{'albun' : albun, 'imagenes' : imagenes}]
        return context


class SubirImagen(LoginRequiredMixin, FormView):
    template_name = 'inicio/subir_imagen.html'
    form_class = ImagenFormulario
    success_url = reverse_lazy('inicio:lista_albun')
    
    def form_valid(self, form):
        nueva_imagen = Imagen(
            imagen = form.cleaned_data['imagen'],
            titulo = form.cleaned_data['titulo'],
            descripcion = form.cleaned_data['descripcion'],
            blog = form.cleaned_data['blog'],
            albun = form.cleaned_data['albun'],
        )
        nueva_imagen.save()
        return super().form_valid(form)
    
    

def imagen_galeria(request):
    albunes = Albun.objects.all()
    albun_data = []
    for albun in albunes:
        albun_imagenes = Imagen.objects.filter(albun=albun)
        albun_data.append({
            'albun':albun,
            'imagenes': albun_imagenes,
        })
    return render(request, 'inicio/imagenes_galeria.html', {'albun_data':albun_data})


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
       