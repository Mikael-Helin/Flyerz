from django.shortcuts import render
from events.models import Event

def landingpage(request):
    events = Event.objects.all()
    return render(request, 'public_pages/landingpage.html', {'user': request.user, 'events': events})
