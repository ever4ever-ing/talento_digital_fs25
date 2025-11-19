from django import forms


CANTIDAD_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CarritoAgregarBicicletaForm(forms.Form):
    """
    Formulario para agregar bicicletas al carrito.
    """
    cantidad = forms.TypedChoiceField(
        choices=CANTIDAD_CHOICES,
        coerce=int,
        label='Cantidad'
    )
    actualizar = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
