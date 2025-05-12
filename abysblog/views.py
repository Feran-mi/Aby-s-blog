from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'index.html', {'full_post': full_post})

def business(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'business.html', {'full_post': full_post})

def sports(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'sports.html', {'full_post': full_post})

def politics(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'politics.html', {'full_post': full_post})

def others(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'others.html', {'full_post': full_post})

def news(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'news.html', {'full_post': full_post})



