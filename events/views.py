from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EventForm, EventCommentForm
from .models import Event, EventAttendance

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
    comments = event.comments.all()
    user_attending = EventAttendance.objects.filter(event=event, attendee=request.user).exists()


    if request.method == 'POST' and 'attend' in request.POST:
        if user_attending:
            messages.warning(request, 'You are already attending this event')
        else:
            EventAttendance.objects.create(event=event, attendee=request.user)
            messages.success(request, 'You are now attending this event')
        return redirect('events:event_details', event_id=event_id)

    if request.method == 'POST' and 'unattend' in request.POST:
        if user_attending:
            EventAttendance.objects.filter(event=event, attendee=request.user).delete()
            messages.success(request, 'You are no longer attending this event')
        else:
            messages.warning(request, 'You are not attending this event')
        return redirect('events:event_details', event_id=event_id)
    

    if request.method == 'POST' and 'comment' in request.POST:
        comment_form = EventCommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.event = event
            comment_form.instance.author = request.user
            comment_form.save()
            return redirect('events:event_details', event_id=event_id) 
    else:
        comment_form = EventCommentForm()
    
    return render(request, 'events/event_details.html', {
        'event': event,
        'comments': comments,
        'comment_form': comment_form,
        'user_attending': user_attending
        })


def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)
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

@login_required
def attend_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user in event.attendees.all():
        messages.warning(request, 'You are already attending this event')
        return redirect('events:event_details', event_id=event_id)
    
    return redirect('events:event_details', event_id=event_id)
