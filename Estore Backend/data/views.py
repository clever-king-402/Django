from django.shortcuts import render
from rest_framework import  viewsets,generics
from .serializers import *
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.models import User
# from Users import User
# Create your views here.

class CategorySet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SliderSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class AdSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class BrandSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductReviewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReview


@api_view(['GET'])
def getCategory(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getSlider(request):
    slider = Slider.objects.all()
    serializer = SliderSerializer(slider,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getAd(request):
    ad = Ad.objects.all()
    serializer = AdSerializer(ad,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getBrand(request):
    brand = Brand.objects.all()
    serializer = BrandSerializer(brand,many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductSale(request,label):
    product = Product.objects.filter(labels= label)
    serializer = ProductSerializer(product,many= True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,slug):
    product = Product.objects.get(slug = slug)
    serializer = ProductSerializer(product,context = {'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    print("ti ma here")
    user = User.objects.create_user(
        username=request.data['userName'],
        email= request.data['email'],
        password=request.data['password'],
    )
    print("ti ma here")
    user.save()
    return Response("this is valid")



class ReviewCRUD(APIView):
    def get(self,request,slug):
        review = ProductReview.objects.filter(slug = slug)
        serializer = ProductReviewSerializer(review,many = True)
        return Response(serializer.data)
    
    def post(self,request,slug):
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response("this is good")
    



