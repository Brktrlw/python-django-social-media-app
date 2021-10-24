from django.shortcuts import render,HttpResponse


def Index(request):
    return HttpResponse("POST ANA SAYFA")

def createPost(request):
    pass

def updatePost(request,postId):
    return HttpResponse(postId)
