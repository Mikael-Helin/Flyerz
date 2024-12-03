from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "search"

urlpatterns = [
    path('', views.search, name='search'),
    path('add_friend', views.add_friend, name='add_friend'),
    path('remove_friend', views.remove_friend, name='remove_friend'),
]
