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
    url = reverse('search:search')
    query = request.POST.get('query', '')
    if query:
        url = f'{url}?query={query}'
    return redirect(url)

# Create your views here.
