"""Bookings models
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    """Model for a booking made by a user."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for Booking model."""
        ordering = ["-date", "-time"]

    def __str__(self):
        return f"Booking for {self.user.username} on {self.date} at {self.time}"
