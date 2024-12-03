from django.urls import path
from . import views


app_name = 'events'
urlpatterns =[
    path('', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('event_details/<int:event_id>/', views.event_details, name='event_details'),
]