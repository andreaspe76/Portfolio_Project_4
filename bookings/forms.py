"""Forms for bookings app
"""

from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and updating bookings."""
    class Meta:
        """Meta class for BookingForm."""
        model = Booking
        fields = ["date", "time", "party_size"]
