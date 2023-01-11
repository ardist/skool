from django.shortcuts import render, redirect
from admins.models import UserProfile

def home(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    context = {'profile':user_profile}

    if not request.user.is_authenticated:
        return redirect('/backend/login')
    else:
        return render(request, 'admins/home.html', context)
