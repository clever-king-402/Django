from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

class Base(View):
    context = {}

class HomeView(Base):
    
    def get(self,request):
        self.context
        self.context['categories'] = Category.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['ads'] = Ad.objects.all()
        self.context["brands"] = Brand.objects.all()
        self.context['hot'] = Product.objects.filter(labels = 'hot')
        self.context['new'] = Product.objects.filter(labels = 'new')
        return render(request,"index.html",self.context)

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")

def myAccount(request):
    return render(request,"my-account.html")

def productList(request):
    return render(request,"product-list.html")

class DetailView(Base):
    def get(self,request,slug):
       self.context
       self.context['products'] = Product.objects.filter(slug = slug)
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


class RegisterView(Base):
    def get(self,request):
        return render(request,"register.html")
    
    def post(self,request):

        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        username = request.POST["userName"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        c_password = request.POST["confirmPassword"]

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"user Exists")
                return redirect("/register")
            if User.objects.filter(email = email).exists():
                messages.error(request,"email Exists")
                return redirect("/register")
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email=email,
                password=password,
                username=username
            )
            user.save()
        else:
            messages.error(request,"wrong password")
        return redirect("/")
    

class LoginView(Base):
    def get(self,request):
        return  render(request,"login.html")
    
    def post(self,request):
        username = request.POST["userName"]
        password = request.POST["password"]
        user = authenticate(request,username = username,password = password)
        if user is not None:
           login(request,user)
           return redirect("/")
        else:
            messages.error(request,"entered wrong password")
            return redirect("/login")
            
def Logout(request):
    logout(request)       
    return redirect("/")