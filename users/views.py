from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegisterForm


def profile(request):
    return render(request, "users/profile.html", {})

def signup(request):
    success_message = None
   
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            success_message = "Your account has been created successfully."
            form = UserRegisterForm()
    else:
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {
        'form': form, 'success_message': success_message})

def login(request):
    return HttpResponse("Heloo world")
