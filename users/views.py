from django.shortcuts import render, redirect, HttpResponse
from users.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from users.models import CustomUser
from django.contrib import messages
from users.services import signin_service, generate_context


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = signin_service(form=form)
        if user:
            login(request, user)
            return redirect("main:index")
        else:
            messages.error(request, "Неверная почта или пароль")
            return redirect("user:signin")
    else:
        form = LoginForm()
        context = generate_context(form=form)
        return render(request, "signin.html", context=context)