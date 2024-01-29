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

# def category(request, cat_slug):
#     category = Categories.objects.get(slug=cat_slug)
#     products = Products.objects.filter(category=category)
#     context = {
#         "products": products
#         }
#     return render(request, "catalog.html", context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product
    }
    return render(request, "product.html", context=context)
