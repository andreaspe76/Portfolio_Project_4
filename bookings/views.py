"""Bookings app views
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


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
            messages.success(request, "Booking created successfully!")
            return redirect("booking_list")
    else:
        form = BookingForm()
    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def booking_list(request):
    """Shows all the bookings for the logged-in user."""
    bookings = Booking.objects.filter(
        user=request.user).order_by('date', 'time')
    return render(request, "bookings/booking_list.html", {"bookings": bookings})


@login_required
def booking_update(request, pk):
    """Allows users to update their bookings."""
    booking = get_object_or_404(
        # Ensures user can only edit their own bookings
        Booking, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully!")
            return redirect("booking_list")
    else:
        form = BookingForm(instance=booking)
    return render(request, "bookings/booking_form.html", {"form": form, "update": True})


@login_required
def booking_delete(request, pk):
    """Allows users to delete their bookings."""
    booking = get_object_or_404(
        # Ensures user can only delete their own bookings
        Booking, pk=pk, user=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted successfully!")
        return redirect("booking_list")
    return render(request, "bookings/booking_confirm_delete.html", {"booking": booking})
