from django.db import models
from store.models import Product
from accounts.models import Account
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank = True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class cartItem(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null = True)
    cart_quantity = models.IntegerField()
    is_active = models.BooleanField(default= True)
    def sub_total(self):
        return self.product.Price * self.cart_quantity


    def __str__(self):
        return self.product.product_name

