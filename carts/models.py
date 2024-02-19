from django.db import models
from users.models import CustomUser
from goods.models import Products

# Create your models here.

class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0



class Cart(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    objects = CartQuerySet.as_manager()

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def product_price(self):
        return round(self.product.sell_price(), 2) * self.quantity

    def __str__(self):
        if self.user:
            return f"User: {self.user} | Product: {self.product.name} | Quantity: {self.quantity}"
        return f"Unauthorized user | Product: {self.product.name} | Quantity: {self.quantity}"

