from django.shortcuts import render
from Post import models
def homePage(request):
    posts=models.Post.objects.all()
    return render(request,"home/index.html",{"posts":posts})

