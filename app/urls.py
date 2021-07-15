from django.urls import path
from .views import *


urlpatterns = [
    path('house/', HouseListAPIView.as_view()),
    path('house/<int:pk>/', HouseRetrieveUpdateDestroyAPIView.as_view()),
    path('house/r/<int:pk>/', HouseRetriveAPIView.as_view()),
    path('house/create/', HouseCreateAPIView.as_view())
]