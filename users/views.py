from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from users.services import signin_service, generate_context, signup_service
from users.models import CustomUser
from users.forms import LoginForm, CreateUserForm



def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = signin_service(form=form)
        if user:
            auth.login(request, user)
            return redirect("main:index")
        else:
            messages.error(request, "Неверная почта или пароль")
            return redirect("user:signin")
    else:
        form = LoginForm()
    context = generate_context(form=form)
    return render(request, "signin.html", context=context)


def registration(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        user = signup_service(form)
        if user:
            auth.login(request, user, backend="users.backends.EmailBackEnd")
            return redirect("main:index")
    else:
        form = CreateUserForm()
    context = generate_context(form=form)
    return render(request, "registration.html", context=context)


def logout(request):
    auth.logout(request)
    return redirect("main:index")
