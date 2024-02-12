from django.shortcuts import render

from home.models import *

# Create your views here.

def homepage(request):
    context = {}
    context["profiles"] = Profile.objects.all()[0]
    return render(request,"index.html",context)

def skillpage(request):
    context = {}
    context["skills"] = Skill.objects.all()
    return render(request,"skills.html",context)

def workpage(request):
    context = {}
    context["works"] = Work.objects.all()
    return render(request,"work.html",context)

def resumepage(request):
    return render(request,"resume.html")