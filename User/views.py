from django.shortcuts import redirect,render
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login

def userLogout(request):           # Çıkış Yapıp Anasayfaya döndürdüğümüz method
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı")
    return redirect("index")

def userLogin(request):
    return render(request, "home/login.html")

def userRegister(request):
    return render(request,"home/register.html")
