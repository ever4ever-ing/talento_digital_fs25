from django import forms
from .models import Event, Participant
from datetime import date


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_date(self):
        d = self.cleaned_data.get('date')
        if d and d <= date.today():
            raise forms.ValidationError('La fecha debe ser futura.')
        return d


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']
