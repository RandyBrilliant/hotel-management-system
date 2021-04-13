from django.shortcuts import render
from .models import FoodMenu

# Create your views here.


def restaurant(request):
    foods = FoodMenu.objects.all()[:4]
    context = {
        'foods': foods,
    }
    return render(request, 'restaurant/restaurant.html', context)
