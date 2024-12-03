from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse

def search(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.POST.get('username', None)
            if username:
                friend_maybe = User.objects.get(username=username)
                if friend_maybe:
                    request.user.friends.add(friend_maybe)
        else:
            print("no username")
        return redirect(reverse('users:search'))
    else:
        query = request.GET.get("q")

        if request.user:
            friends = request.user.friends.all() 
        else:
            friends = []

        if not query:
            search_result = []
        else:
            search_result = User.objects.filter(
                    Q(username__icontains=query)
                )

        return render(request, 'users/search.html', {
            "search_result": search_result,
            "friends": friends,
        })

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
