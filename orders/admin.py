from django.contrib import admin
from orders.models import Order, OrderItem

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "status")


# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
admin.site.register(OrderItem)
