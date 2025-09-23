"""Bookings app views
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


# Create your views here.
def home(request):
    """Renders the home page."""
    return render(request, 'home.html')


def menu(request):
    """Renders the menu page."""
    return render(request, 'menu.html')


@login_required
def booking_create(request):
    """Renders the booking form."""
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("booking_list")
    else:
        form = BookingForm()
    return render(request, "bookings/booking_form.html", {"form": form})
