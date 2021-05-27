from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity_of_rooms']