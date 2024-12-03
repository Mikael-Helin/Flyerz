from django.urls import path
from . import views


app_name = 'events'
urlpatterns =[
    path('', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
]