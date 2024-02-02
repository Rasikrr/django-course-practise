from goods.models import Products, Categories
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator


def get_products_by_category(category_slug):
    """Получить все товары с определенным слагом"""
    goods = Products.objects.all()
    if category_slug != "all":
        category = get_category_by_slug(category_slug)
        goods = get_list_or_404(goods.filter(category=category))
    return goods

def get_single_product_by_slug(product_slug):
    """Получить товар по слагу"""
    product = Products.objects.get(slug=product_slug)
    return product

def get_filtered_products(goods, on_sale, order_by):
    """Получить отфильтрованные товары"""
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
    return goods

def get_category_by_slug(category_slug):
    """Получить категорию по слагу"""
    return Categories.objects.get(slug=category_slug)


def make_context(**kwargs):
    """Формирование контекста для Views"""
    return kwargs

