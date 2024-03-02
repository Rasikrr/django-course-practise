from django.db import models
from users.models import CustomUser
from goods.models import Products

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, verbose_name="Пользователь", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delievery = models.BooleanField(default=False, verbose_name="Требутеся доставка")
    delievery_address = models.TextField(null=True, blank=True, verbose_name="Адресс доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default='В обработке', verbose_name="Статус заказа")


    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.pk} | Покупатель: {self.user.first_name} {self.user.last_name}"


class OrderItemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True,
                                verbose_name="Товар")
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    objects = OrderItemQuerySet.as_manager()

    def product_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f"Товар: {self.product.name} | Заказ №{self.order.pk}"

