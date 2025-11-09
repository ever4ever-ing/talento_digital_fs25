from django import forms
from .models import Automovil

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'año', 'precio', 'disponible']
        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Toyota, Ford, Chevrolet'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Corolla, Focus, Cruze'
            }),
            'año': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 2010,
                'max': 2025,
                'placeholder': 'Año de fabricación'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '100000',
                'min': 1000000,
                'placeholder': 'Precio en pesos'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'marca': 'Marca del vehículo',
            'modelo': 'Modelo',
            'año': 'Año de fabricación',
            'precio': 'Precio (CLP)',
            'disponible': 'Disponible para venta'
        }
        help_texts = {
            'precio': 'Ingrese el precio en pesos chilenos',
            'año': 'Año entre 2010 y 2025'
        }