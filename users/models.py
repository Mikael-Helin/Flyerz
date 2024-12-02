from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError

class User(AbstractUser):
    friends = models.ManyToManyField("self", symmetrical=False)
    email = models.EmailField(unique=True)
    # Add file field
    profile_picture = models.ImageField(
        upload_to= "profile_pics",
        blank=True,
        null=True
    )

# ADDED BY MIKAEL
class Friend(models.Model):
    user_1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friendships_as_user_1'
    )
    accepted_time_1 = models.DateTimeField(null=True, blank=True)

    user_2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friendships_as_user_2'
    )
    accepted_time_2 = models.DateTimeField(null=True, blank=True)

    class Meta:
        # The Meta class contains a UniqueConstraint on the user_1 and user_2 fields to ensure that each pair of users can only have one Friend instance.
        constraints = [
            models.UniqueConstraint(
                fields=['user_1', 'user_2'],
                name='unique_friendship'
            )
        ]

    def clean(self):
        # Ensure user_1 < user_2
        if self.user_1 == self.user_2:
            raise ValidationError("user_1 and user_2 cannot be the same.")
        if self.user_1.id > self.user_2.id:
            self.user_1, self.user_2 = self.user_2, self.user_1

    def save(self, *args, **kwargs):
        # Call clean to ensure the user_1 < user_2 rule
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Friendship between {self.user_1} and {self.user_2}"
