from django.shortcuts import render
from room.models import RoomType
from user.models import UserFeedback

# Create your views here.


def home(request):
    rooms = RoomType.objects.all()
    feedbacks = UserFeedback.objects.filter(featured=True)
    context = {
        'rooms': rooms,
        'feedbacks': feedbacks
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html', {})
