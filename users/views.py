from django.shortcuts import render, HttpResponse, HttpResponseRedirect


def login(request):
    return render(request, "login.html")

def registration(request):
    return render(request, "registration.html")

def profile(request):
    return render(request, "profile.html")

def logout(request):
    pass

