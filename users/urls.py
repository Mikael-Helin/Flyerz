from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='profile'),
    path('login/', views.login_view, name='login'),
]
