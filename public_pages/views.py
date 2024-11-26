from django.shortcuts import render

def landingpage(request):
    return render(request, 'public_pages/landingpage.html', {})
