from django.contrib import admin
from django.urls import  path
from home.views import homePage, windowpage, xboxPage

urlpatterns = [
    path('',homePage,name="homepage"),
    path('xbox/',xboxPage,name="xboxPage"),
    path('window/',windowpage,name="windows"),
    

]
