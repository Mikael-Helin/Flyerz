from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path("change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change_password.html",
            success_url="change-password-done/"  # redirect to this page after successful password change
        ),
        name="change_password"
    ),
    path("change-password/change-password-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done_a.html"
        ),
        name="password_change_done"
    ), #https://docs.djangoproject.com/en/5.1/topics/auth/default/#module-django.contrib.auth.views
    path("delete-user/<int:pk>/", views.DeleteUserView.as_view(), name="delete_user"),
]
