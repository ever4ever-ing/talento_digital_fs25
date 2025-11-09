from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'is_private', 'allowed_users']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'allowed_users': forms.SelectMultiple(),
        }