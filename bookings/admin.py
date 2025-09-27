"""Admin configuration for the bookings app."""

from django.contrib import admin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin view for the Booking model."""

    list_display = ('user', 'date', 'time', 'party_size')
    list_filter = ('date', 'time')
    search_fields = ('user__username',)


# Define any additional control permissions here.

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser
