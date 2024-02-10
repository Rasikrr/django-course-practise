from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories, Products
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator
from goods.services.services import *
# Create your views here.


def catalog(request, category_slug=None):
    # Get page number
    print(request.GET)
    page = request.GET.get("page", "1")

    if not page.isdigit():
        page = 1
    page = int(page)

    # Get filters
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("query", None)

    # Get products and filters
    goods = get_products_by_category(category_slug)
    goods = get_filtered_products(goods, on_sale, order_by, query)

    # Pagination
    paginator = Paginator(goods, 3)
    current_page = paginator.get_page(page)

    context = make_context(goods=current_page, slug_url=category_slug)

    return render(request, "catalog.html", context=context)


def product(request, product_slug):
    product = get_single_product_by_slug(product_slug)
    context = make_context(product=product)
    return render(request, "product.html", context=context)


