from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello")