from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

# Create your views here.
def event(request):
    event_details = Event
    return render(request, 'events/event.html', {event_details: event_details})

def event_list(request):
    sort_by = request.GET.get('sort_by', 'date')
    event_list = Event.objects.all().order_by(sort_by)
    return render(request, 'events/event_list.html', {'event_list': event_list})

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