from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'is_authed': False,
        'form':form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Sign up',
        'is_authed': False,
        'form':form,
    }
    return render(request, 'users/registration.html', context)

def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')
            return HttpResponseRedirect(reverse('users:profile_edit'))
    else:
        form = UserProfileForm(instance=request.user)
        
    context = {
        'title': 'Profile Settings',
        'is_authed': False,
        'form': form,
    }
    return render(request, 'users/profile_edit.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))