from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone
from decimal import Decimal

from .models import Automovil

CURRENT_YEAR = timezone.now().year

matricula_validator = RegexValidator(
    regex=r'^[A-Z0-9\-]{4,8}$',
    message='Matrícula inválida. Solo letras, números y guiones (4-8 caracteres).',
    code='invalid_matricula'
)

class AutomovilForm(forms.Form):
    marca = forms.CharField(
        max_length=50,
        label='Marca',
        widget=forms.TextInput(attrs={'placeholder': 'p. ej. Toyota'})
    )
    modelo = forms.CharField(
        max_length=50,
        label='Modelo'
    )
    anio = forms.IntegerField(
        label='Año',
        validators=[MinValueValidator(1900), MaxValueValidator(CURRENT_YEAR)],
        help_text=f'Entre 1900 y {CURRENT_YEAR}'
    )
    precio = forms.DecimalField(
        label='Precio',
        max_digits=10,
        decimal_places=2,
        min_value=Decimal('0.00')
    )
    matricula = forms.CharField(
        label='Matrícula',
        max_length=8,
        validators=[matricula_validator]
    )
    disponible = forms.BooleanField(
        label='Disponible',
        required=False,
        initial=True
    )

    def clean_matricula(self):
        m = self.cleaned_data.get('matricula', '')
        return m.strip().upper()

    def clean(self):
        cleaned = super().clean()
        precio = cleaned.get('precio')
        anio = cleaned.get('anio')

        if precio is not None and precio <= 0:
            self.add_error('precio', 'El precio debe ser mayor que 0.')

        if anio is not None and (anio < 1900 or anio > CURRENT_YEAR):
            self.add_error('anio', f'El año debe estar entre 1900 y {CURRENT_YEAR}.')

        return cleaned

class AutomovilModelForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'anio', 'precio', 'matricula', 'disponible']
        widgets = {
            'marca': forms.TextInput(attrs={'placeholder': 'p. ej. Toyota'}),
            'modelo': forms.TextInput(),
        }
        help_texts = {
            'anio': f'Entre 1900 y {CURRENT_YEAR}',
        }

    def clean_matricula(self):
        m = self.cleaned_data.get('matricula', '')
        matricula_validator(m)
        return m.strip().upper()

    def clean(self):
        cleaned = super().clean()
        precio = cleaned.get('precio')
        anio = cleaned.get('anio')

        if precio is not None and precio <= 0:
            self.add_error('precio', 'El precio debe ser mayor que 0.')

        if anio is not None and (anio < 1900 or anio > CURRENT_YEAR):
            self.add_error('anio', f'El año debe estar entre 1900 y {CURRENT_YEAR}.')

        return cleaned