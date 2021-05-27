from rest_framework import generics, permissions
from .models import House
from .serializers import HouseSerializer, HouseCreateSerializer

class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (permissions.AllowAny, )

class HouseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseCreateAPIView(generics.CreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseCreateSerializer

class HouseUpdateAPIView(generics.UpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseDeleteAPIView(generics.DestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer