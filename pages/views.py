from django.shortcuts import render
from .models import Post, Category

def index(request):   
    posts = Post.objects.all()
    context ={'posts': posts}    
    return render(request, 'pages/index.html', context)

def detailPost(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:3]
    categories = Category.objects.all()
    context ={'post': post, 'posts': posts, 'categories': categories}
    return render(request, 'pages/detail.html', context)
