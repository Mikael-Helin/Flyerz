from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login


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

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                redirect('/')
            else:
                print('bad username password')
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "users/login.html", context)
