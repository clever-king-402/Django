from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
# Create your views here.

class Base(View):
    context = {}

class HomeView(Base):
    
    def get(self,request):
        self.context = {}
        self.context['categories'] = Category.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['ads'] = Ad.objects.all()
        self.context['hot'] = Product.objects.filter(labels = 'hot')
        self.context['new'] = Product.objects.filter(labels = 'new')
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

class DetailView(Base):
    def get(self,request,slug):
       self.context
       self.context['products'] = Product.objects.filter(slug = slug)
       print(self.context['products'])
       return render(request,"product-detail.html",self.context)

    def post(self,request,slug):
        self.context
        if request.method == "POST":
            name = request.POST['username']
            email = request.POST['email']
            review = request.POST['review']
            data = ProductReview.objects.create(
                name = name,
                email = email,
                review = review,
                slug = slug,
                rating = 1
            )
            data.save()
            self.context['reviews'] = ProductReview.objects.filter(slug=slug)
        return render(request,"product-detail.html",self.context)


def wishlist(request):
    return render(request,"wishlist.html")

