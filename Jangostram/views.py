from django.shortcuts import render
from Post import models,forms

def homePage(request):
    posts=models.Post.objects.all()
    form=forms.CommentForm(request.POST or None)
    return render(request,"home/index.html",{"posts":posts,"form":form})


