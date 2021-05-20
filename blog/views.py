from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-createDate')
    return render(request, 'home.html', {'posts': posts})


def detail(request, postId):
    post = get_object_or_404(Post, pk=postId)
    return render(request, 'detail.html', {'post': post})
