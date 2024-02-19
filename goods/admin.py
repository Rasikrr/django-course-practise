from django.contrib import admin
from goods import models
# Register your models here.

@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", )

@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "category", "price", "quantity", "discount")
    list_editable = ("discount",)
    search_fields = ("name", "description","category__name")
    list_filter = ("discount", "category")
    fields = (
        "name",
        "category",
        "description",
        "slug",
        "image",
        ("price", "discount"),
        "quantity"
        )
