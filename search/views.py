from django.shortcuts import HttpResponse, render


def search(request):
    return render(request, "search/search.html", {})

# Create your views here.
