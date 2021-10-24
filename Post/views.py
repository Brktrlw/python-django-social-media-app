from django.shortcuts import render,HttpResponse


def Index(request):
    return render(request,"home/index.html")

def createPost(request):
    pass

def updatePost(request,postId):
    return HttpResponse(postId)
