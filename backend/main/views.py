from django.shortcuts import render
from room.models import RoomType

# Create your views here.


def home(request):
    rooms = RoomType.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html', {})
