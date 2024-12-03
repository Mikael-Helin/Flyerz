from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

# Create your views here.
def event(request):
    event_details = Event
    return render(request, 'events/event.html', {event_details: event_details})

def event_list(request):
    sort_by = request.GET.get('sort_by', 'date')
    events = Event.objects.all().order_by(sort_by)
    return render(request, 'events/eventlist.html', {'events': events})


def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_details.html', {'event': event})

def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        event_form.instance.organizer = request.user

        if event_form.is_valid():
            event_form.save()
            return redirect('events:event_details', event_id=event_form.instance.id)

    else:
        event_form = EventForm()
        print("GET request received")
    return render(request, 'events/add_event.html', {'event_form': event_form})


def user_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/user_events.html', {'events': events})


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
