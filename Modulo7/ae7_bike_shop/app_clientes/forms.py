from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Cliente, PerfilCliente


class ClienteRegistroForm(UserCreationForm):
    """Formulario para registrar nuevos usuarios (clientes)"""
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('nombre', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre Completo'
        self.fields['email'].label = 'Correo Electrónico'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Usar email como username
        user.first_name = self.cleaned_data['nombre']
        if commit:
            user.save()
            # Crear cliente asociado
            Cliente.objects.get_or_create(
                email=user.email,
                defaults={'nombre': user.first_name}
            )
        return user


class ClienteLoginForm(AuthenticationForm):
    """Formulario de inicio de sesión"""
    username = forms.EmailField(label='Correo Electrónico')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Correo Electrónico'
        self.fields['password'].label = 'Contraseña'


class PerfilClienteForm(forms.ModelForm):
    """Formulario para actualizar el perfil del cliente"""
    class Meta:
        model = PerfilCliente
        fields = ('direccion', 'telefono', 'fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'telefono': forms.TextInput(attrs={'type': 'tel'}),
        }
