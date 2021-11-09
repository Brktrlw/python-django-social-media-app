from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Index(request):
    return render(request,"home/index.html")

@login_required(login_url="userLogin")
def postDetail(request):
    return render(request,"home/postDetail.html") # postDetail.html dosyasını oluştur

@login_required(login_url="userLogin")
def createPost(request):
    form=PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            newPost=form.save(commit=False)
            newPost.postAuthor=request.user
            newPost.save()
            messages.success(request,"Başarıyla paylaşıldı")
            return redirect("index")
    else:
        return redirect("index")
    return render(request,"home/index.html")

def updatePost(request,postId):
    return
