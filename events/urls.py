from django.urls import path
from . import views


urlpatterns =[
    path('', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
]