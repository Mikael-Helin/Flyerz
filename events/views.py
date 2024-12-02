from django.http import HttpResponse
from django.shortcuts import render
from .forms import EventForm

# Create your views here.
def event(request):
    return render(request, 'events/event.html')

def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        event_form.instance.organizer = request.user

        print('USER', request.user)
         
        if event_form.is_valid():
           
           event_form.save()
           return HttpResponse("Event added successfully.")
    else:
        event_form = EventForm()
        print("GET request received")
    return render(request, 'events/add_event.html', {'event_form': event_form})