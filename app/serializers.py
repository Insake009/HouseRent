from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'image', 'city', 'price', 'area', 'quantity_of_rooms', 'phone', 'users_id']

class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'city', 'price', 'area', 'quantity_of_rooms', 'phone', 'users_id']