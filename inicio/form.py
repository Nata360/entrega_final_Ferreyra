from django import forms
from .models import *
from ckeditor.fields import RichTextFormField

class BuscarBlogFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
class CrearAlbunFormulario(forms.ModelForm):
    class Meta:
        model = Albun
        fields = ['titulo', 'autor', 'blog']

class ImagenFormulario(forms.ModelForm):
    descripcion = RichTextFormField(max_length=800)
    class Meta:
        model = Imagen
        fields = ['albun', 'imagen', 'titulo', 'descripcion', 'blog']

class EditarImagenFormulario(forms.ModelForm):
    descripcion = RichTextFormField(max_length=800)
    class Meta:
        model = Imagen
        fields = ['titulo', 'descripcion']

class EditarAlbunFormulario(forms.ModelForm):
    class Meta:
        model = Albun
        fields = ['titulo']