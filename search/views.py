from django.shortcuts import HttpResponse, render


def search(request):
    query = request.GET.get('query', '')
    context = {
        "query": query
    }
    return render(request, "search/search.html", context)

# Create your views here.
