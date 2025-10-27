from django import forms
from .models import Automovil

class AutomovilModelForm(forms.ModelForm):
    """
    Formulario basado en el modelo Automovil.
    Django genera automáticamente los campos desde el modelo.
    """
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'anio', 'precio', 'matricula', 'disponible']