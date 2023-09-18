from django.urls import path 
from .views import post_list, post_detail 

urlpatterns = [
    path('', post_list),
    path('post/<int:pk>/', post_detail),
]