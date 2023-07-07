from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
# Create your views here.

def home(request):
    return render(request, "main/home.html")
    

class contact(ListView):
    template_name = "main/contact.html"
 


def about(request):
    return render(request, "main/about.html")


def bmi(request):
    return render(request, "main/bmi.html")

    
class blog(ListView):
    template_name = "main/blog.html"

def diet(request):
    return render(request, "main/diet.html")

def workout(request):
    return render(request, "main/workout.html")

def portfolio(request):
    return render(request, "main/portfolio.html")

def blog(request):
    return render(request, "main/blog.html")
