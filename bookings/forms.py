"""Forms for bookings app
"""

import datetime
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and updating bookings."""
    time = forms.ChoiceField(choices=[
        ('14:00', '14.00'),
        ('14:30', '14.30'),
        ('15:00', '15.00'),
        ('15:30', '15.30'),
        ('16:00', '16.00'),
        ('16:30', '16.30'),
        ('17:00', '17.00'),
        ('17:30', '17.30'),
        ('18:00', '18.00'),
        ('18:30', '18.30'),
        ('19:00', '19.00'),
        ('19:30', '19.30'),
        ('20:00', '20.00'),
        ('20:30', '20.30'),
        ('21:00', '21.00'),
        ('21:30', '21.30'),
    ])
    party_size = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 9)])

    class Meta:
        """Meta class for BookingForm."""
        model = Booking
        fields = ["date", "time", "party_size"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control",
                                           "min": datetime.date.today().strftime("%Y-%m-%d")}),
        }
