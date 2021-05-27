from django.urls import path
from .views import *


urlpatterns = [
    path('house/', HouseListAPIView.as_view()),
    path('house/<int:pk>/', HouseRetrieveAPIView.as_view()),
    path('house/create/', HouseCreateAPIView.as_view()),
    path('house/update/<int:pk>/', HouseUpdateAPIView.as_view()),
    path('house/delete/<int:pk>/', HouseDeleteAPIView.as_view())
]