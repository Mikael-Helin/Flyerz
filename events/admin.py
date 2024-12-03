from django.contrib import admin
from .models import Event, EventAttendance, EventComment

# Register your models here.
admin.site.register(Event)
admin.site.register(EventAttendance)
admin.site.register(EventComment)
