from django.contrib import admin
from .models import Room, RoomType


class RoomTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('room_name',)}  # new


# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType, RoomTypeAdmin)
