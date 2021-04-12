from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'customer', 'booking_date', 'status']
    search_fields = ['room_name']


admin.site.register(Booking, BookingAdmin)
