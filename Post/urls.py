from django.urls import path
import Post.views
from .views import createPost,Index

urlpatterns = [
    path('',Index),
    path('create/',Index),
    path('update/', Index),
]