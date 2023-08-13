from django import forms
from .models import *
from ckeditor.fields import RichTextFormField

class BuscarBlogFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
class BuscarAlbunFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
class CrearBlogFormulario(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
    
class CrearAlbunFormulario(forms.ModelForm):
    class Meta:
        model = Albun
        fields = ['titulo', 'blog']



class ImagenFormulario(forms.ModelForm):
    descripcion = RichTextFormField(max_length=800)
    
    def __init__(self, user, *args, **kwargs):
        super(ImagenFormulario, self).__init__(*args, **kwargs)
        self.fields['albun'].queryset = Albun.objects.filter(autor=user)
        self.fields['blog'].queryset = Blog.objects.filter(autor=user)
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