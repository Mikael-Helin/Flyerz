from django.shortcuts import render, redirect, reverse
from users.models import User
from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')

    users = []
    if query:
        users = User.objects.filter(
            Q(username__icontains=query)
        )

    context = {
        "query": query,
        "users": users,
    }

    return render(request, "search/search.html", context)

def add_friend(request):
    return redirect(reverse('search:search'))

# Create your views here.
