from django import forms
from .models import Blog, AlbunImagen

class FormularioSubirImagen(forms.ModelForm):
    
    class Meta:
        model = AlbunImagen
        fields = 'albun', 'imagen'

