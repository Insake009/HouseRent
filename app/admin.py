from django.contrib import admin
from .models import House, Comment, Like

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity_of_rooms']

admin.site.register(Comment)

admin.site.register(Like)
