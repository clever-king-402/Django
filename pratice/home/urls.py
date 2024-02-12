from ast import pattern
from django.conf import settings
from django.contrib import admin
from django.urls import  path
from home.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name="homepage"),
    path('skills/',skillpage,name="skill"),
    path('work/',workpage,name="work"),
    path('resume/',resumepage,name="resume"),
    

]
