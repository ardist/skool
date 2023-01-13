from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.contrib import messages
from admins.models import UserProfile
from pages.models import Post, Category
from .forms import PostForm

def home(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    context = {'profile':user_profile}

    if not request.user.is_authenticated:
        return redirect('/backend/login')
    else:
        return render(request, 'admins/home.html', context)

@login_required
def listPost(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    context = {'profile':user_profile}
    posts = Post.objects.all()
    context ={'posts':posts, 'profile':user_profile}
    return render(request, 'admins/list.html', context)

@login_required
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('posting')
    context = {'form': form}
    return render(request, 'admins/create.html', context)

@login_required
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()     
            messages.success(request, "Posting success to updated!")       
            return redirect('posting')
    context = {'form': form}
    return render(request, 'admins/update.html', context)

@login_required
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':       
        post.delete()
        messages.success(request, "Posting success to delete!")
        return redirect('posting')
    context = {'form': form, 'post': post}
    return render(request, 'admins/delete.html', context)