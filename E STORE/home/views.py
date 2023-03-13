from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
# Create your views here.

class HomeView(View):
    
    def get(self,request):
        self.context = {}
        self.context['categories'] = Category.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['ads'] = Ad.objects.all()
        return render(request,"index.html",self.context)

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def myAccount(request):
    return render(request,"my-account.html")

def productList(request):
    return render(request,"product-list.html")

def productDetail(request):
    return render(request,"product-detail.html")

def wishlist(request):
    return render(request,"wishlist.html")

