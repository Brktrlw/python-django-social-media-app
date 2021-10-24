from django.shortcuts import render,HttpResponse

def homePage(request):         # Ana sayfanın açılmasını sağlayan method
    return HttpResponse("naber")

