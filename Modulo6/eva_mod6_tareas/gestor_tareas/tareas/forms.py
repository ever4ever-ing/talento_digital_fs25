from django import forms
from .models import Tarea

class TareaForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Título de la tarea'
        })
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Descripción de la tarea'
        }),
        required=False
    )


class TareaModelForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción de la tarea'}),
            # 'fecha_vencimiento' and 'prioridad' removed in simplified model
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }