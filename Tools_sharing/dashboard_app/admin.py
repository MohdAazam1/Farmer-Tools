from django.contrib import admin
from bookings.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tool', 'created_at')
