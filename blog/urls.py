from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('', post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('login/', BlogLoginView.as_view(),name='login'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # path('post/<int:pk>/', post_detail, name='post_detail'),
    # path('post/create/', post_new, name='post_create'),
    # path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('categories/', category_list, name='category_list'),
    
]

urlpatterns += staticfiles_urlpatterns()