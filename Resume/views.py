from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.


def home(request):
    return render(request, "home.html")


def project(request):
    return render(request,"project.html")


def about(request):
    return render(request, "about.html")
    

def resume(request):
    return render(request, "resume.html")

