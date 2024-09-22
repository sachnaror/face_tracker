# tracking/urls.py
from django.urls import path

from . import views

# tracking/urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('add_face/', views.add_recognized_face, name='add_face'),
]
