from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def team(request):
    return HttpResponse("This is the team page.")
