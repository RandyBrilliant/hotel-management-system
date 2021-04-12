from django.contrib import admin
from .models import Room, RoomType


class RoomTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('room_name',)}
    list_display = ['room_name', 'edited_room_price', 'date_updated']

    def edited_room_price(self, obj):
        return "Rp. {}".format(obj.room_price)

    search_fields = ['room_name']


class RoomNoAdmin(admin.ModelAdmin):
    readonly_fields = ['date_added', 'date_updated']
    list_display = ['room_no', 'room_type', 'status']
    list_filter = ['status']
    search_fields = ['room_no']
    ordering = ['room_no']
    filter_horizontal = ()


# Register your models here.
admin.site.register(Room, RoomNoAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
