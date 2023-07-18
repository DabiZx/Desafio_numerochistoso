from django import forms

from .models import Articulos

class CrearArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields=[
            'titulo',
            'contenido',
            'categoria'


        ]