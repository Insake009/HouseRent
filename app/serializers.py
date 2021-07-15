from rest_framework import serializers
from .models import House, Comment

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'house_id']


class HouseSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True, source='hous_id')

    class Meta:
        model = House
        fields = ['id', 'image', 'city', 'price', 'area', 'quantity_of_rooms',
                  'phone', 'user_id', 'comments']