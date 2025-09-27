"""Bookings app URLs
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('new/', views.booking_create, name='booking_create'),
    path('my-bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:pk>/edit/', views.booking_update, name='booking_update'),
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]
