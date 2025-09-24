"""Bookings app URLs
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('new/', views.booking_create, name='booking_create'),
    path('my_bookings/', views.booking_list, name='booking_list'),
]
