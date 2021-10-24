from django.urls import path
import Post.views
from .views import createPost,Index,updatePost

urlpatterns = [
    path('',Index),
    path('create/',createPost),
    path('update/<int:postId>', updatePost),
]