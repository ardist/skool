from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView 
from . import views

urlpatterns = [      
    path('', LoginView.as_view(template_name='admins/login.html'), name='login'),
    path('login', LoginView.as_view(template_name='admins/login.html'), name='login'), 
    path('home', views.home, name='home'),
    path('posting', views.listPost, name='posting'),
    path('create', views.createPost, name='create'),
    path('update/<str:slug>', views.updatePost, name='update'),
    path('delete/<str:slug>', views.deletePost, name='delete'),
]
