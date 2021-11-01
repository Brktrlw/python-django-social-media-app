from django.urls import path
from .views import userLogout,userLogin,userRegister,userProfile,userProfilePage

urlpatterns = [
    path('logout/',userLogout,name="userLogout"),
    path('login/',userLogin,name="userLogin"),
    path('register/',userRegister,name="userRegister"),
    path('profile/',userProfile,name="userProfile"),
    path('<string:userNickName>',userProfilePage,name="userProfilePage")
]