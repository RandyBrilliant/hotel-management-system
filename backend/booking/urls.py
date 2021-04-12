from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.CheckBookingPage, name="check-page"),
    path('check/booking/', views.BookingPage, name="booking-page"),
]
