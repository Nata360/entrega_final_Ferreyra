from django import forms
from .models import *

class BuscarBlogFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
class CrearAlbunFormulario(forms.ModelForm):
    class Meta:
        model = Albun
        fields = ['titulo', 'autor', 'blog']

class ImagenFormulario(forms.ModelForm):
    descripcion = models.CharField(max_length=200)
    class Meta:
        model = Imagen
        fields = ['albun', 'imagen', 'titulo', 'descripcion', 'blog']