from django.contrib import admin
from .models import Payment,Order,OrderProduct
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','payment_id','payment_method','amount_paid','status']
    list_filter = ['user','payment_id','status']

class orderAdmin(admin.ModelAdmin):
    list_display = ['user','order_number','email','order_total']
    list_filter = ['order_number','status']

class orderproductAdmin(admin.ModelAdmin):
    list_display = ['user','payment','ordered']
    list_filter = ['updated_at','user']

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct)