from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.services import signin_service, generate_context, signup_service, profile_edit_service, add_anonymous_user_cart
from users.models import CustomUser
from users.forms import LoginForm, CreateUserForm, ProfileForm



def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = signin_service(form=form)
        if user:
            auth.login(request, user)

            add_anonymous_user_cart(request=request, user=user)

            messages.success(request, "Вы успешно вошли в аккаунт")
            redirect_page = request.POST.get("next", None)
            if redirect_page and redirect_page != reverse("user:logout"):
                return redirect(redirect_page)
            return redirect("main:index")
        else:
            messages.warning(request, "Неверная почта или пароль")
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

            add_anonymous_user_cart(request=request, user=user)

            auth.login(request, user, backend="users.backends.EmailBackEnd")
            messages.success(request, "Вы успешно зарегестрированы и вошли в аккаунт")
            return redirect("main:index")
    else:
        form = CreateUserForm()
    context = generate_context(form=form)
    return render(request, "registration.html", context=context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user, files=request.FILES)
        response = profile_edit_service(form)
        if response:
            print("YESS")
            messages.success(request, "Данные успешно обновлены")
            return redirect("user:profile")
    else:
        form = ProfileForm()
    context = generate_context(form=form)
    return render(request, "profile.html", context=context)

def users_cart(request):
    return render(request, "users/users_cart.html")

def logout(request):
    auth.logout(request)
    messages.success(request, "Вы успешно вышли из аккаунты")
    return redirect("main:index")
