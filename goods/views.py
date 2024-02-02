from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories, Products
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator
from goods.services.services import *
# Create your views here.


def catalog(request, category_slug, page=1):
    goods = get_products_by_category(category_slug)
    paginator = Paginator(goods, 3)
    current_page = paginator.get_page(page)
    context = {
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "catalog.html", context=context)


def product(request, product_slug):
    product = get_single_product_by_slug(product_slug)
    context = {
        "product": product
    }
    return render(request, "product.html", context=context)


