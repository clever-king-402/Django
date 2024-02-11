from django.shortcuts import render

from home.models import *

# Create your views here.

def homePage(request):
    context = {}
    context['users'] = User.objects.all()
    context['ads'] = Ad.objects.all()
    return render(request,'index.html',context)

def xboxPage(request):
    return render(request,"game.html")

def windowpage(request):
    return render(request,'windows.html')