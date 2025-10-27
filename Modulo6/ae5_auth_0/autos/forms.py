from django import forms
from .models import Automovil

class AutomovilForm(forms.ModelForm):
    class Meta: #Meta indica que es una clase interna que contiene información adicional sobre la clase principal.
        model = Automovil
        fields = ['marca', 'modelo', 'anio', 'precio', 'disponible']