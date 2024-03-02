from carts.models import Cart
from django.db import transaction
from django.shortcuts import render, redirect
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from users.services import generate_context
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# # Create your views here.

@login_required
def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    carts_items = Cart.objects.filter(user=user)

                    if carts_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            requires_delievery=form.cleaned_data["requires_delivery"],
                            delievery_address=form.cleaned_data["delivery_address"],
                            payment_on_get=form.cleaned_data["payment_on_get"]
                        )
                        for cart_item in carts_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.product.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточно количество товара {name} на складе В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        carts_items.delete()
                        messages.success(request, "Заказ успешно создан")
                        return redirect("main:index")
            except ValidationError as e:
                print("NO")
                messages.success(request, str(e))
                return redirect("cart:order")

    else:
        initial = generate_context(first_name=request.user.first_name,
                                   last_name=request.user.last_name)
        form = CreateOrderForm(initial=initial)

    context = generate_context(title="Home: Оформление заказа", form=form, order=True)
    return render(request, "orders/create_order.html", context=context)
