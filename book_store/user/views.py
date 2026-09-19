from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, ProfileForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Saytga kirdingiz!")
            return redirect('all_books')
    else:
        form = LoginForm()
    context = {
        "user_form": form
    }
    return render(request, "user/auth.html", context)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account ochildi.\nIltimos login qilib kiring!")
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        "register_form": form
    }
    return render(request, "user/auth.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Siz accountdan chiqdingiz!")
    return redirect('login')


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile ma'lumotlari o'zgartirilidi!")
    return render(request, "user/profile.html")