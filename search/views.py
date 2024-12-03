from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from users.models import User

def search(request):
    query = request.GET.get('query', '')

    users = []

    if query:
        users = User.objects.filter(
            Q(username__icontains=query)
        )

    friends = []

    if request.user.is_authenticated:
        friends = request.user.friends.all()

    context = {
        "query": query,
        "users": users,
        "friends": friends,
    }

    return render(request, "search/search.html", context)

@login_required
def add_friend(request):
    param_query = request.POST.get('query', None)
    param_friend_id = request.POST.get('friend_id', None)

    if param_friend_id:
        friend = User.objects.get(id=param_friend_id)
        if friend:
            friend.friends.add(request.user)
            friend.save()

    url = reverse('search:search')

    if param_query:
        url = f'{url}?query={param_query}'

    return redirect(url)

@login_required
def remove_friend(request):
    param_query = request.POST.get('query', None)
    param_friend_id = request.POST.get('friend_id', None)

    if param_friend_id:
        friend = User.objects.get(id=param_friend_id)
        if friend:
            friend.friends.remove(request.user)
            friend.save()

    url = reverse('search:search')

    if param_query:
        url = f'{url}?query={param_query}'

    return redirect(url)

# Create your views here.
