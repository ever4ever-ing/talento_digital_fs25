from django import forms
from .models import Automovil

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'año', 'precio', 'disponible']
        widgets = {
            'año': forms.NumberInput(attrs={'min': 2010, 'max': 2020}),
            'precio': forms.NumberInput(attrs={'step': '100000', 'min': 2000000}),
        }