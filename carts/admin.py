from django.contrib import admin
from carts.models import Cart

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user_display", "product", "quantity", "created_timestamp")
    list_filter = ("created_timestamp", "user", "product")
    def user_display(self, obj):
        print(obj.user)
        if obj.user:
            return str(obj.user.email)
        return "Anonymous user"

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ("product", "quantity", "created_timestamp")
    search_fields = fields
    readonly_fields = ("created_timestamp",)
    extra = 1
