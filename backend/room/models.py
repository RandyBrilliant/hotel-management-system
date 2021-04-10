from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.urls import reverse
from django_resized import ResizedImageField

# Create your models here.


class RoomType(models.Model):
    room_type = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    room_name = models.CharField(max_length=200)
    room_img = ResizedImageField(size=[800, 525], crop=['middle', 'center'], quality=100,
                                 default="room_img/default.jpg", upload_to="room_img")
    description = RichTextField()
    room_price = models.DecimalField(max_digits=19, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'slug': self.slug})

    @property
    def imageURL(self):
        try:
            url = self.room_img.url
        except:
            url = ''
        return url


class Room(models.Model):
    OCCUPIED = "OCP"
    CLEANED = "CLN"
    AVAILABLE = "AVA"
    OFF = "OFF"
    STATUS = [
        (OCCUPIED, 'Occupied'),
        (CLEANED, 'Clean'),
        (AVAILABLE, 'Available'),
        (OFF, 'Off'),
    ]
    room_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_no = models.IntegerField(blank=False, null=False, unique=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        verbose_name="Room Status",
        default=AVAILABLE
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.room_no)
