from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories, Products
# Create your views here.


def catalog(request):
    goods = Products.objects.all()
    context = {
        "goods": goods
    }
    return render(request, "catalog.html", context=context)

def product(request):
    return render(request, "product.html")
