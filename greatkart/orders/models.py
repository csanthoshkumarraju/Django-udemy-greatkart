from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=150)
    amount_paid = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self) :
        return self.status
    
class Order(models.Model):
    status = (
        ('New','New',),
        ('Accepted','Accepted',),
        ('Completed','Completed',),
        ('Cancelled','Cancelled',),
    )
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=150)
    amount_paid = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    order_number = models.CharField(max_length=150)
    first_name  = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address_line1 = models.CharField(max_length=150)
    address_line2 = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    order_note = models.CharField(max_length=150)
    order_total = models.FloatField(max_length=150)
    tax_total = models.FloatField( max_length = 500)

    def __str__(self) :
        return self.user.first_name
    
class OrderProduct(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=50)
    product_price = models.FloatField(max_length=50)
    ordered = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)