from django.shortcuts import render
from post.models import article,Category
from django.urls import reverse

def home(request):
    Articles = article.objects.all()
    recent_articles=article.objects.all().order_by("-created")
    category=Category.objects.all()

    return render(request,'home/home.html',{'Articles':Articles,"recent_articles":recent_articles,"category":category})

def AboutUs(request):
    return render(request,"home/AboutUs.html")
