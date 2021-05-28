from django.urls import path
from .views import *


urlpatterns = [
    path('house/', HouseListAPIView.as_view()),
    path('house/<int:pk>/', HouseRetrieveAPIView.as_view()),
    path('house/create/', HouseCreateAPIView.as_view()),
    # path('house/comments/', CommentCreateAPIView.as_view()),
    path('house/like/<int:pk>/', LikeAPIView.as_view())
]