from django.urls import path
from .views import createPost,Index,updatePost,postDetail
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',Index),
    path('create/',createPost),
    path('<int:postId>',postDetail),
    path('update/<int:postId>', updatePost),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
