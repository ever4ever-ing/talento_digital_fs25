from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Ingresa el título del evento'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe tu evento'
            }),
            'fecha_inicio': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'fecha_fin': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ubicación del evento'
            }),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha y Hora de Inicio',
            'fecha_fin': 'Fecha y Hora de Término',
            'ubicacion': 'Ubicación',
        }
