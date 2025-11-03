from django import forms
from .models import Event, Participant


# Formulario para crear eventos
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


# Formulario para agregar participantes
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']
        
