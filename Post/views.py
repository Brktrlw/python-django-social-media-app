from django.shortcuts import render,HttpResponse
from .forms import PostForm
from .models import Post
def Index(request):
    return render(request,"home/index.html")

def createPost(request):
    form=PostForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            newPost=form.save(commit=False)
            newPost.postAuthor=request.user
            newPost.save()
    return render(request,"home/index.html",{"form":form})

def updatePost(request,postId):
    return HttpResponse(postId)
