from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from inicio.models import *
from inicio.form import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')


class CrearBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'inicio/crear_blog.html'
    fields = ['nombre_blog', 'nombre_autor', 'apellido_autor', 'categoria', 'descripcion',]
    success_url = reverse_lazy('inicio:lista_blogs')
    
    def form_valid(self, form):
        
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
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
    
    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(autor=self.request.user)
    def get(self, request,*args, **kwargs):
        blog = self.get_object()
 
        if blog.autor != self.request.user:
            return redirect('inicio:no_puedes_borrar_blog') 
        return super().get(request, *args, **kwargs)
    
        
def no_puedes_borrar_blog(request):
    return render(request, 'inicio/no_puedes_borrar_blog.html')
        
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
            form.instance.autor = self.request.user
            
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        

class ListaAlbun(ListView):
    model = Albun
    template_name = 'inicio/lista_albun.html'
    context_object_name = 'albunes'
    
    def get_queryset(self):
        listado_albun = []
        formulario = BuscarBlogFormulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['nombre']
            listado_albun = Blog.objects.filter(nombre_blog__icontains=nombre_a_buscar)
        return listado_albun
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarAlbunFormulario
        return contexto
    
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

class EliminarAlbun(LoginRequiredMixin, DeleteView):
    model = Albun
    template_name = 'inicio/eliminar_albun.html'
    success_url = reverse_lazy('inicio:lista_albun')
    
    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(autor=self.request.user)
    
    
@login_required
def editar_albun(request, pk):
    albun = get_object_or_404(Albun, pk=pk)
    if albun.autor == request.user:
        if request.method == 'POST':
            formulario = EditarAlbunFormulario(request.POST, instance=albun)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio:ver_albun', pk=albun.pk)
        else:
            formulario = EditarAlbunFormulario(instance=albun)
        return render(request, 'inicio/editar_albun.html', {'formulario': formulario, 'albun': albun})
    else:
        return HttpResponseForbidden('No tienen permiso para editar este álbum')    


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

@login_required
def eliminar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    if imagen.albun.autor == request.user:
        imagen.delete()
    
    return redirect('inicio:ver_albun', pk=imagen.albun.pk)

@login_required
def editar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    if imagen.albun.autor == request.user:
        if request.method == 'POST':
            formulario= EditarImagenFormulario(request.POST, instance=imagen)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio:ver_albun', pk=imagen.albun.pk)
        else:
            formulario = EditarImagenFormulario(instance=imagen)
        return render(request, 'inicio/editar_imagen.html', {'formulario':formulario, 'imagen':imagen})
    else:
        return HttpResponseForbidden('No tienen permiso para editar esta imagen')



