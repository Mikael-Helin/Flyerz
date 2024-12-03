from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EventForm
from .models import Event

# Create your views here.
def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        event_form.instance.organizer = request.user

        print('USER', request.user)

        if event_form.is_valid():
            new_event = event_form.save()

            events = Event.objects.filter(organizer=request.user)

            return render(request, 'events/user_events.html', {'events': events})
    else:
        event_form = EventForm()
        print("GET request received")
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/add_event.html', {'event_form': event_form})


def user_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/user_events.html', {'events': events})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/eventlist.html', {'events': events})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:user_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('events:user_events')
    
    return render(request, 'events/confirm_delete.html', {'event': event})
