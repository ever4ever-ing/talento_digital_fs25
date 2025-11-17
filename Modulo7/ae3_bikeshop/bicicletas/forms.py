from django import forms
from .models import Bicicleta

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = '__all__'
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }