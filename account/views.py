from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import LoginForm,UserEditForm,RegForm
from django.contrib.auth.forms import UserCreationForm


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('/')
    if request.method == "POST":
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account_app:login")
    else:
        form=RegForm()
    return render(request,"account/reg.html",{"form":form})

def user_logout(requst):
    logout(requst)
    return redirect('/')

def user_edit(request):
    user=request.user
    form=UserEditForm(instance=user)
    if request.method == "POST":
        form=UserEditForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()

    return render(request,"account/edit.html",{"form":form})
def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=User.objects.get(username=form.cleaned_data.get("username"))
            login(request,user)
            return redirect("home_app:home")
    else:
        form=LoginForm()
    return render(request, "account/login.html", {"form":form})

