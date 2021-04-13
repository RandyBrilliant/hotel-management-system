from django.contrib import admin
from .models import FoodMenu

# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'menu_price',
                    'date_added', 'status']
    list_filter = ['status']
    search_fields = ['menu_name']


admin.site.register(FoodMenu, FoodAdmin)
