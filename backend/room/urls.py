from django.urls import path

from .views import RoomDetailView

urlpatterns = [
    path('<slug:slug>', RoomDetailView.as_view(), name='room_detail'),
]
