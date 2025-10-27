from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        }),
        error_messages={
            'required': 'Por favor, ingresa tu nombre.'
        }
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        }),
        error_messages={
            'required': 'Por favor, ingresa tu email.',
            'invalid': 'Por favor, ingresa un email válido.'
        }
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje aquí...',
            'rows': 5
        }),
        error_messages={
            'required': 'Por favor, escribe un mensaje.'
        }
    )
