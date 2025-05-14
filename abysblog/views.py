from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    f_post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'f_post': f_post})

