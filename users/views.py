from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib import auth


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username, password)
        if user:
            auth.login(request, user)
            return redirect("main:index")
        else:
            return redirect("user:signin")
        # if form.is_valid():
        #     print("1232")
        #     return redirect("main:index")
        # else:
        #     print(form.error_messages, form.errors)
        #     print("INVALID")
        #     return redirect("user:signin")
    else:
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "signin.html", context=context)