from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories, Products
# Create your views here.


def catalog(request):
    categories = Categories.objects.all()
    context = {"categories": categories}
    return render(request, "catalog.html")

def product(request):
    return render(request, "product.html")
