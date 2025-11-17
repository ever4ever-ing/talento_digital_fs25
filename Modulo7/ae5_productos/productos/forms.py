# productos/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Incluimos los campos que queremos que aparezcan en el formulario
        fields = ['nombre', 'precio', 'disponible']
