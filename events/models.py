from django.db import models
from users.models import User

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