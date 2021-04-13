from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

# Create your models here.


class FoodMenu(models.Model):
    AVAILABLE = "AVA"
    OUT = "OUT"
    STATUS = [
        (AVAILABLE, 'Available'),
        (OUT, 'Out of Stock'),
    ]

    menu_name = models.CharField(max_length=200)
    menu_description = RichTextField()
    menu_img = ResizedImageField(size=[800, 525], crop=['middle', 'center'], quality=100,
                                 default="food_img/default.jpg", upload_to="food_img")
    menu_price = models.DecimalField(max_digits=19, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        verbose_name="Menu Status",
        default=AVAILABLE
    )

    def __str__(self):
        return self.menu_name

    @property
    def imageURL(self):
        try:
            url = self.menu_img.url
        except:
            url = ''
        return url
