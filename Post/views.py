from django.shortcuts import render,redirect
from .forms import PostForm

def Index(request):
    return render(request,"home/index.html")

def createPost(request):
    form=PostForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            newPost=form.save(commit=False)
            newPost.postAuthor=request.user
            newPost.save()
    else:
        return redirect("index")
    return render(request,"home/index.html")

def updatePost(request,postId):
    return
