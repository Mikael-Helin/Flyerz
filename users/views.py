from django.http import HttpResponse
from django.shortcuts import render

def profile(request):
    return render(request, "users/profile.html", {})

def signup(request):
    return render(request, "registration/signup.html", {})
