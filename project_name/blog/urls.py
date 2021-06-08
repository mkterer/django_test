from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('ddd', views.dddd, name='aaa'),
    path('add', views.advans, name='aaa'),
]