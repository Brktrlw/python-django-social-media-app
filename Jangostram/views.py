from django.shortcuts import render

def homePage(request):                              # Ana sayfanın açılmasını sağlayan method
    return render(request,"home/index.html")

