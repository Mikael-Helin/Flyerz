from django.urls import path
from . import views

app_name = 'events'

app_name = 'events'
urlpatterns =[
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('event_details/<int:event_id>/', views.event_details, name='event_details'),
    path('user_events/', views.user_events, name='user_events'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]