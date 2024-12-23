from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def profile(request):
    user_details = User
    return render(request, 'users/profile.html', {user_details: user_details})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def edit_profile(request):
    if 'action' in request.POST:
        if request.POST['action'] == 'save':
            user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Your profile has been updated successfully.")
                return redirect('users:profile')
        elif request.POST['action'] == 'cancel':
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        print("Initial values in form:", user_form.initial) # Debugging

    return render(request, 'users/edit_profile.html', {'user_form': user_form})

class DeleteUserView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        print("DeleteUserView accessed")
        logout(request)
        messages.success(request, "Your account has been deleted successfully.")
        return super().delete(request, *args, **kwargs)
    
def users_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/users_profile.html', {'user': user})