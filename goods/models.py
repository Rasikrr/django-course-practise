from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    slug = models.SlugField(max_length=256, blank=True, unique=True, null=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    slug = models.SlugField(max_length=256, blank=True, unique=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(default="sq.jpg",upload_to="goods_image", blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в процентах")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)

    def __str__(self):
        return self.name
    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})






