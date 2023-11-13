
from django.contrib import admin
from django.urls import path
from app.views import create_feature_vector,index,image_detail, search_images,list_images

urlpatterns = [
   path('create/', create_feature_vector, name='create'),
   path('index/', index, name='index'),
   path("images/", list_images, name='images'),
   path('get/<int:id>', image_detail, name='detail_image'),
   path('search/', search_images, name='search_images'),
]


