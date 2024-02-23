from django.db import models
from users.models import CustomUser

# Create your models here.
class Order(models.Model):
    status_choices = {
        "PR": "В обработке",
        "FN": "Доставлен"
    }

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delievery = models.BooleanField(default=False, verbose_name="Требутеся доставка")
    delievery_address = models.TextField(null=True, blank=True, verbose_name="Адресс доставки")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=20, choices=status_choices, default=status_choices.get("PR"))


    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.pk} | Покупатель: {self.user.first_name} {self.user.last_name}"


