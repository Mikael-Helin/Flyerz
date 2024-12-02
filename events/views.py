from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def event(request):
    return HttpResponse("This is the event page.")