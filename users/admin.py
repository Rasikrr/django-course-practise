from django.contrib import admin
from users.models import CustomUser
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    list_display_links = list_display
    search_fields = list_display
    list_filter = ("is_staff", "is_active")

    inlines = [CartTabAdmin, OrderTabulareAdmin]