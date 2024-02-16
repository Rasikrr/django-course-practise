from goods.models import Products
from carts.models import Cart

def add_to_cart(product_id, user):
    product = Products.objects.get(id=product_id)
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user, product=product)
        if not cart.exists():
            cart = Cart.objects.create(user=user, product=product, quantity=1)
        else:
            cart = cart.first()
            cart.quantity += 1
        cart.save()


def remove_from_cart(cart_id, user):
    cart = Cart.objects.get(id=cart_id)
    quantity_deleted = cart.quantity
    cart.delete()
    return get_user_carts(user=user), quantity_deleted


def change_cart_quantity(cart_id, quantity, user):
    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    return get_user_carts(user=user)



def get_user_carts(request=None, user=None):
    if user is None:
        user = request.user
    return Cart.objects.filter(user=user)
