from django.shortcuts import render
from Post import models
from django.http import JsonResponse
def homePage(request):
    posts=models.Post.objects.all()
    return render(request,"home/index.html",{"posts":posts})


def berkayResponse(request):
    sozluk={
        "ad":"berkay",
        "soyad":"sen"
    }
    return JsonResponse(sozluk)