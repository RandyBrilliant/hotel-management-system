from django.shortcuts import render
from .models import RoomType
from django.views.generic import ListView, DetailView
from django.db.models import Q


# Create your views here.
class RoomDetailView(DetailView):
    model = RoomType
    template_name = 'room/room_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        context['otherrooms'] = RoomType.objects.filter(~Q(
            room_type=self.object.room_type))
        return context
