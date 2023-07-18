from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from inicio.models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
    

# @login_required
# def subir_imagen_view(request):
#     if request.method == 'POST':
#         formulario = FormularioSubirImagen(request.POST, request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             mensaje = '¡La imagen se ha subido correctamente!'
#     else:
#         formulario = FormularioSubirImagen()
        
#     return 

# @login_required
# def crear_albun(request):
#     info_extra_user = request.user.infoextra
#     if request.method == 'POST':
#         formulario = FormularioCrearAlbun(request.POST, request.FILES, instance= request.user)
#         if formulario.is_valid():
#             formulario.save()
#             mensaje = '¡El albun se ha creado correctamente!'
#     else:
#         formulario = FormularioCrearAlbun()
#     return render(request, 'inicio/subir_imagenes/crear_albun.html', {'formulario':formulario})

# def home_view(request):
#     return render('base.html')