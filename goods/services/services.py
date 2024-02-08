from goods.models import Products, Categories
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline


def get_products_by_category(category_slug):
    """Получить все товары с определенным слагом"""
    goods = Products.objects.all()
    if category_slug and category_slug != "all":
        category = get_category_by_slug(category_slug)
        goods = goods.filter(category=category)
    return goods

def get_single_product_by_slug(product_slug):
    """Получить товар по слагу"""
    product = Products.objects.get(slug=product_slug)
    return product

def get_filtered_products(goods, on_sale, order_by, query):
    """Получить отфильтрованные товары"""
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
    if query:
        # if query.isdigit() and len(query) <= 5:
        #     goods = goods.filter(id=int(query))
        # else:
        vector = SearchVector("name", "description")
        query = SearchQuery(query)
        goods = goods.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
        goods = goods.annotate(
            headline=SearchHeadline(
                "name",
                query,
                start_sel='<span style=background-color: yellow;>',
                stop_sel="</span>")
        )

        goods = goods.annotate(
            bodyline=SearchHeadline(
                "description",
                query,
                start_sel='<span style=background-color: yellow;>',
                stop_sel="</span>")
        )
    return goods


def get_category_by_slug(category_slug):
    """Получить категорию по слагу"""
    return Categories.objects.get(slug=category_slug)


def make_context(**kwargs):
    """Формирование контекста для Views"""
    return kwargs

