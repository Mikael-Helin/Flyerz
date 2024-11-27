from django.urls import path
from . import views
from .views import friend_map # ADDED BY MIKAEL

app_name = "users"

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('friend-map/', views.friend_map, name='friend_map'), # ADDED BY MIKAEL
]
