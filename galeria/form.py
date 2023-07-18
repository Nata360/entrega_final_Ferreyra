from django import forms
from .models import *

class ImagenFormulario(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen', 'titulo']