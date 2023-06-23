from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from food.models import Profile


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'Username is not available!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                profile = Profile()
                profile.person = user
                profile.save()
                auth.login(request, user)
                return redirect('home')
        else:
                return render(request, 'account/signup.html', {'error': 'Passwords must match!'})

    else:
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'username and password do not match!'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
