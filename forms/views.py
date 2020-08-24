from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegisterForm

def home(request):
    return HttpResponse("<h1>Welcome to django</h1>")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render (response, "register.html", {"form":form})
