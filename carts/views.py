from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from goods.models import Products
from carts.services import get_user_carts
from carts.models import Cart
from carts import services

# Create your views here.


def cart_add(request):
    product_id = request.POST.get("product_id")
    user_carts = services.add_to_cart(product_id, request)
    cart_items_html = rerender_cart(request, user_carts)
    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html
    }
    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    user_carts = services.change_cart_quantity(cart_id, quantity, request)
    cart_items_html = rerender_cart(request, user_carts)
    response_data = {
        "message": "Количество товара было изменено",
        "cart_items_html": cart_items_html
    }
    return JsonResponse(response_data)



def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    user_carts, quantity_deleted = services.remove_from_cart(cart_id=cart_id, request=request)
    cart_items_html = rerender_cart(request, user_carts)
    response_data = {
        "message": "Товар был удален из корзины",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity_deleted
    }
    return JsonResponse(response_data)


def rerender_cart(request, user_carts):
    return render_to_string("carts/includes/included_cart.html", {"carts": user_carts}, request=request)

