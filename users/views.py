from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm
from users.models import User
from django.contrib.auth.decorators import login_required

def profile(request):
    user_details = User
    return render(request, "users/profile.html", {user_details: user_details})

@login_required
def edit_profile(request):
    current_user = request.user
    success_message = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            success_message = "Your profile has been updated successfully."
    else:
        user_form = UserUpdateForm(instance=current_user)

    return render(request, "users/edit_profile.html", {
        'user_form': user_form,
        'success_message': success_message
    })

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

