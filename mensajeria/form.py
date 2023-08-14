from django import forms
from mensajeria.models import *


class FormularioMensajeria(forms.ModelForm):
    class Meta:
        model = Mensajeria
        fields = ['contenido']
        
