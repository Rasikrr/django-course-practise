from goods.models import Products
from carts.models import Cart

def add_to_cart(product_id, request):
    product = Products.objects.get(id=product_id)
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user, product=product)
        if not cart.exists():
            cart = Cart.objects.create(user=user, product=product, quantity=1)
        else:
            cart = cart.first()
            cart.quantity += 1
        cart.save()
        return get_user_carts(user=user)
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1
            )
        return get_user_carts(request=request)


def remove_from_cart(cart_id, request):
    cart = Cart.objects.get(id=cart_id)
    quantity_deleted = cart.quantity
    cart.delete()
    if request.user.is_authenticated:
        return get_user_carts(user=request.user), quantity_deleted
    return get_user_carts(request=request), quantity_deleted


def change_cart_quantity(cart_id, quantity, request):
    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    if request.user.is_authenticated:
        return get_user_carts(user=request.user)
    return get_user_carts(request=request)



def get_user_carts(request=None, user=None):
    if user is None:
        user = request.user
    if user.is_authenticated:
        return Cart.objects.filter(user=user)
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)


