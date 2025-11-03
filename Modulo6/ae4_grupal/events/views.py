from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from .forms import EventForm, ParticipantForm
from .models import Event, Participant

def register_event(request):
    ParticipantFormSet = modelformset_factory(Participant, form=ParticipantForm, extra=2)
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        formset = ParticipantFormSet(request.POST, queryset=Participant.objects.none())
        if event_form.is_valid() and formset.is_valid():
            event = event_form.save()
            for form in formset:
                participant = form.save(commit=False)
                participant.event = event
                participant.save()
            return render(request, 'events/success.html', {'event': event})
    else:
        event_form = EventForm()
        formset = ParticipantFormSet(queryset=Participant.objects.none())
    return render(request, 'events/register.html', {'event_form': event_form, 'formset': formset})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk) # Se maneja errores
    return render(request, 'events/detail.html', {'event': event})