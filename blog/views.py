from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5:-1]
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_filter(request, str):
    posts_filter = Post.objects.filter(them=str).filter(published_date__lte=timezone.now()).order_by('published_date')[:5:-1]
    return render(request, 'blog/post_list.html', {'posts': posts_filter})

def month_archive(request, year, month):
    posts = Post.objects.filter(published_date__year=year).filter(published_date__month=month)
    return render(request, 'blog/post_list.html', {'posts': posts})
