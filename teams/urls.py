from django.urls import path
from . import views

app_name = "teams"

urlpatterns = [
    path('', views.team, name='team'),
]
    