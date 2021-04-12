from django.db import models
from room.models import Room
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.


class Booking(models.Model):
    CHECKIN = "CI"
    CHECKOUT = "CO"
    RESERVED = "RS"
    PAID = "PD"
    STATUS = [
        (CHECKIN, 'Check In'),
        (CHECKOUT, 'Check Out'),
        (RESERVED, 'Reserved'),
        (PAID, 'Paid'),
    ]

    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        verbose_name="Booking Status",
        default=RESERVED
    )

    def __str__(self):
        return str(self.booking_id)

    def customer_name(self):
        return str(self.customer.username)
