from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Post, Category

def index(request):   
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:       
        posts = paginator.page(1)
    except EmptyPage:        
        posts = paginator.page(paginator.num_pages)
    context ={'posts': posts, 'pages':page}    
    return render(request, 'pages/index.html', context)

def detailPost(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:3]
    categories = Category.objects.all()
    context ={'post': post, 'posts': posts, 'categories': categories}
    return render(request, 'pages/detail.html', context)
