from django.urls import path
from .views import RoomDetailView, RoomListView

urlpatterns = [
    path('<slug:slug>', RoomDetailView.as_view(), name='room_detail'),
    path('', RoomListView.as_view(), name='room-list'),
]
