from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Booking
from room.models import RoomType, Room
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import uuid

# Create your views here.


def CheckBookingPage(request):
    if request.method == 'POST' or 'submit' in request.POST:
        check_in_date = request.POST.get("checkIn")
        check_out_date = request.POST.get("checkOut")
    else:
        check_in_date = datetime.date(datetime.now()).strftime('%Y-%m-%d')
        check_out_date = datetime.date(
            datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    booking_no_room = Booking.objects.filter(
        check_in__gte=check_in_date, check_out__lte=check_out_date).values('room__room_no')
    room_available = Room.objects.exclude(
        room_no__in=booking_no_room).order_by('room_type')
    rooms = RoomType.objects.filter(
        rooms_count__in=room_available).distinct()
    print(rooms)

    room_type_grouped = {}

    for changelog in room_available:
        current_key = changelog.room_type
        room_type_grouped.setdefault(current_key, []).append(changelog)

    context = {
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'rooms': rooms,
        'room_type_grouped': room_type_grouped
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
    else:
        return redirect('check-page')


@login_required
def CompletePage(request):
    if request.method == 'POST' or 'submit' in request.POST:
        check_in_date = request.POST.get("checkIn")
        check_out_date = request.POST.get("checkOut")
        chosen_room = request.POST.get("room_type")
        guest_detail = request.user

        booking_no_room = Booking.objects.filter(
            check_in__gte=check_in_date, check_out__lte=check_out_date).values('room__room_no')
        room_available = Room.objects.exclude(
            room_no__in=booking_no_room).filter(room_type=uuid.UUID(chosen_room)).first()

        final = Booking(
            room=room_available,
            customer=guest_detail,
            check_in=check_in_date,
            check_out=check_out_date,
        )

        Booking.save(final)

        booking = Booking.objects.latest('booking_id')
        context = {
            'booking': booking,
        }
        return render(request, 'booking/complete.html', context)
    else:
        return redirect('check-page')
