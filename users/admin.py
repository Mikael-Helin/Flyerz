from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.register(User, UserAdmin)

# ADDED BY MIKAEL
from .models import Friend
admin.site.register(Friend)