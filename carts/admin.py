from django.contrib import admin
from carts.models import Cart

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "created_timestamp")
    list_display_links = list_display
