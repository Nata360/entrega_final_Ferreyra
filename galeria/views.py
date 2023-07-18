from django.shortcuts import render, redirect
from .models import *
from .form import *

# Create your views here.

# def subir_imagen(request):
#     if request.method == 'GET':
#         return render(request, 'subir_imagen.html')
#     elif request.method == 'POST':
#         formulario = ImagenFormulario(request.POST, request.FILES)
#         if formulario.is_valid():
#             nueva_imagen = Imagen(imagen = formulario.cleaned_data['imagen'], titulo = formulario.cleaned_data['titulo'])
#             nueva_imagen.save()
#             return redirect('galeria:imagen_galeria.html')
def subir_imagen(request):
    if request.method == 'POST':
        formulario = ImagenFormulario(request.POST, request.FILES)
        # autor = request.user
        if formulario.is_valid():
            
            nueva_imagen = Imagen(imagen = formulario.cleaned_data['imagen'], titulo = formulario.cleaned_data['titulo'])
            nueva_imagen.save()
            
            # mensaje = '¡La imagen se ha subido correctamente!'
        return render(request, 'subir_imagen.html', {'formulario':formulario})    
    else:
        formulario = ImagenFormulario()
            
    return render(request, 'subir_imagen.html', {'formulario':formulario})        

        
def imagen_galeria(request):
    imagenes = Imagen.objects.all()
    print(imagenes)
    return render(request, 'imagen_galeria.html', {'imagenes':imagenes})