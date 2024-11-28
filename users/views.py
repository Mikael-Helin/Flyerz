from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegisterForm, LoginForm


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
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            pass
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "users/login.html", context)
