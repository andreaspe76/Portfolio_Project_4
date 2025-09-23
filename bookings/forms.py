"""Forms for bookings app
"""

from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and updating bookings."""
    party_size = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 9)])

    class Meta:
        """Meta class for BookingForm."""
        model = Booking
        fields = ["date", "time", "party_size"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control",
                                           "step": 1800}),
        }
