from django.contrib import admin
from carts.models import Cart,cartItem
# Register your models here.
class cartItemAdmin(admin.ModelAdmin):
    list_display = ['user','product','cart_quantity']
    list_filter = ['is_active','cart_quantity']

admin.site.register(Cart)
admin.site.register(cartItem,cartItemAdmin)
