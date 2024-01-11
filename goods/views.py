from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def catalog(request):
    return render(request, "catalog.html")

def product(request):
    return render(request, "product.html")
