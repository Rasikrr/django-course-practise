from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from goods.models import Products
from carts.models import Cart

# Create your views here.


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)
        if not cart.exists():
            cart = Cart.objects.create(user=request.user, product=product, quantity=1)
        else:
            cart = cart.first()
            cart.quantity += 1
        cart.save()

    return redirect(request.META["HTTP_REFERER"])



def cart_change(request, product_slug):
    pass

def cart_remove(request, product_slug):
    pass