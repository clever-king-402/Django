from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request,'index.html')

def xboxPage(request):
    return render(request,"game.html")

def windowpage(request):
    return render(request,'windows.html')