# autos/forms.py
from django import forms
from .models import Automovil

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'anio', 'precio', 'disponible']