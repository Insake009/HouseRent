from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import House
from .serializers import *


class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (permissions.AllowAny, )


class HouseRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class LikeAPIView(generics.GenericAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def post(self, request, *args, **kwargs):
        print(request.user)
        house_id = request.data.get('house')
        house = House.objects.filter(id=house_id).first()
        house.likes += 1
        print(house.likes)
        house.save()
        return Response('House liked', status=status.HTTP_202_ACCEPTED)

class HouseCreateAPIView(generics.CreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def create(self, request, *args, **kwargs):
        serializer_data = request.data
        data = {**serializer_data, "user_id": request.user}

        d = House.objects.create(
            image=data['image'][0],
            city=data['city'][0],
            price=data['price'][0],
            area=data['area'][0],
            quantity_of_rooms=data['quantity_of_rooms'][0],
            phone=data['phone'][0],
            user_id=request.user
        )
        print(d)
        return Response('created', status=status.HTTP_201_CREATED)

