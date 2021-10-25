from django.shortcuts import redirect,render
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User

def userLogout(request):           # Çıkış Yapıp Anasayfaya döndürdüğümüz method
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı")
    return redirect("index")

def userLogin(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=name,password=password)
        if user is None:
            messages.warning(request,"Hatalı kullanıcı bilgileri,lütfen tekrar deneyiniz")
            return render(request,"home/login.html",{"form":form})
        else:
            messages.success(request,"Başarıyla giriş yaptınız")
            login(request,user)
            return redirect("index")
    return render(request, "home/login.html",{"form":form})

def userRegister(request):
    form = RegisterForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            newUser = User(username=username, email=email)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Başarıyla kayıt olundu")
            return redirect("index")
        else:
            return render(request, "home/register.html", {"form": form})
    else:
        return render(request, "home/register.html", {"form": form})


