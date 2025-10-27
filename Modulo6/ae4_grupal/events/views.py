from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .forms import EventForm, ParticipantForm
from .models import Participant, Event
from django.db.utils import OperationalError


def register_event(request):
    ParticipantFormSet = modelformset_factory(Participant, form=ParticipantForm, extra=1, can_delete=False)

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        formset = ParticipantFormSet(request.POST, queryset=Participant.objects.none())
        if event_form.is_valid() and formset.is_valid():
            event = event_form.save()
            for f in formset:
                if f.cleaned_data.get('name'):
                    participant = f.save(commit=False)
                    participant.event = event
                    participant.save()
            return render(request, 'events/success.html', {'event': event})
    else:
        event_form = EventForm()
        formset = ParticipantFormSet(queryset=Participant.objects.none())

    return render(request, 'events/register.html', {'event_form': event_form, 'formset': formset})


def event_list(request):
    try:
        # Obtener todos los eventos con sus participantes para evitar consultas adicionales
        events = Event.objects.all().prefetch_related('participants') 
    except OperationalError:
        # DB/tables not ready: show minimal instruction to run migrations
        return render(request, 'events/db_error.html')
    return render(request, 'events/list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/detail.html', {'event': event})
