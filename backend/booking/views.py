from django.shortcuts import render
from .models import Booking
from room.models import RoomType, Room
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.


def CheckBookingPage(request):
    if request.method == 'POST' or 'submit' in request.POST:
        check_in_date = request.POST.get("checkIn")
        check_out_date = request.POST.get("checkOut")

        booking = Booking.objects.filter(
            check_in__gte=check_in_date, check_out__lte=check_out_date).count()

        booking_no_room = Booking.objects.filter(
            check_in__gte=check_in_date, check_out__lte=check_out_date).values('room__room_no')
        print(booking_no_room)
        room_available = Room.objects.exclude(room_no__in=booking_no_room)
        print(room_available)
        rooms = RoomType.objects.filter(
            rooms_count__in=room_available).distinct()
        print(rooms)

        # if booking == 0:
        #     rooms = room_available
        # elif booking > 0:
        #     rooms = RoomType.objects.exclude(
        #         rooms_count__room_no__in=booking_no_room)

        context = {
            'booking': booking,
            'check_in_date': check_in_date,
            'check_out_date': check_out_date,
            'room_available': room_available,
            'rooms': rooms,
        }

        return render(request, 'booking/check.html', context)


@login_required
def BookingPage(request):
    if request.method == 'POST' or 'submit' in request.POST:
        check_in_date = request.POST.get("checkIn")
        check_out_date = request.POST.get("checkOut")
        chosen_room = request.POST.get("room_type")

        fmt = '%Y-%m-%d'
        nights = datetime.strptime(
            check_out_date, fmt) - datetime.strptime(check_in_date, fmt)

        final_rooms = RoomType.objects.filter(room_name=chosen_room)

        context = {
            'check_in_date': check_in_date,
            'check_out_date': check_out_date,
            'final_rooms': final_rooms,
            'nights': nights
        }

    return render(request, 'booking/booking.html', context)
