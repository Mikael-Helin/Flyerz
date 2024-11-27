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


# ADDED BY MIKAEL
from .models import Friend
from django.contrib.auth import get_user_model
def friend_map(request):
    User = get_user_model()
    users = list(User.objects.all())  # List of all user objects

    # Create a flat dictionary to hold friendship timestamps
    friendship_map = {}
    for row in Friend.objects.all():
        user_1 = row.user_1.username
        user_2 = row.user_2.username
        time_1 = row.accepted_time_1
        time_2 = row.accepted_time_2

        # Use concatenated keys for simplicity
        friendship_map[f"{user_1}-{user_2}"] = time_1
        friendship_map[f"{user_2}-{user_1}"] = time_2

    return render(request, 'friend_map.html', {
        'users': users,
        'friendship_map': friendship_map,
    })
