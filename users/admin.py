from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdmin(UserAdmin):
    model = User
    
    fieldsets = UserAdmin.fieldsets + (
        ('Profile Picture', {'fields': ('profile_picture',)}),
        ('Friendship Details', {'fields': ('friends',)}),
    )
    

admin.site.register(User, UserAdmin)


# ADDED BY MIKAEL
# from .models import Friend
# admin.site.register(Friend)
