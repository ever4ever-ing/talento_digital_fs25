from django import forms
from .models import Resena


class ResenaForm(forms.ModelForm):
    """
    Formulario para crear y editar reseñas
    """
    PUNTUACION_CHOICES = [
        (1, '⭐ 1 estrella - Muy malo'),
        (2, '⭐⭐ 2 estrellas - Malo'),
        (3, '⭐⭐⭐ 3 estrellas - Regular'),
        (4, '⭐⭐⭐⭐ 4 estrellas - Bueno'),
        (5, '⭐⭐⭐⭐⭐ 5 estrellas - Excelente'),
    ]

    puntuacion = forms.ChoiceField(
        choices=PUNTUACION_CHOICES,
        widget=forms.RadioSelect,
        label='Calificación'
    )

    class Meta:
        model = Resena
        fields = ['puntuacion', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Cuéntanos tu experiencia con esta bicicleta...',
                'class': 'form-control'
            })
        }
        labels = {
            'comentario': 'Tu comentario'
        }
