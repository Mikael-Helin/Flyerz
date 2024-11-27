from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegisterForm
from users.models import User
from django.contrib.auth.decorators import login_required


def profile(request):
    user_details = User
    return render(request, "users/profile.html", {user_details: user_details})

@login_required
def edit_profile(request):
    return HttpResponse("Edit your profile here.")

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

