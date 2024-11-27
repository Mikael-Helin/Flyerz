from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
