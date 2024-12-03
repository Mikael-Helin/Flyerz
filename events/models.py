from django.db import models
from users.models import User
from django.db.models.fields import IntegerField

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=250)
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    event_flyer = models.ImageField(
        upload_to='event_flyerz',
        blank=True,
        null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'date'],
                name='unique_event'
            )
        ]
        ordering = ['date']

    def __str__(self) :
        return self.title + " by " + self.organizer.username
    
class EventComment(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.event.title}"
    

class EventAttendance(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='attendees'
    )
    attendee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='attended_events'
    )
    amount_of_guests = IntegerField(default=0) #https://docs.djangoproject.com/en/5.1/intro/tutorial04/

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'attendee'],
                name='unique_attendance'
            )
        ]

    def __str__(self):
        return f"{self.attendee.username} attended {self.event.title}"