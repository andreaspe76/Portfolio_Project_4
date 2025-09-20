"""Bookings app views
"""

from django.shortcuts import render


# Create your views here.
def home(request):
    """Renders the home page."""
    return render(request, 'home.html')


def menu(request):
    """Renders the menu page."""
    return render(request, 'menu.html')
