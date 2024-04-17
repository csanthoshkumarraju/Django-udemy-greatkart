from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
# Create your models here.

class Product(models.Model):
    product_name        = models.CharField(max_length=200,unique= True)
    slug                = models.SlugField(max_length=200,unique=True)
    product_description = models.TextField(max_length=500,blank = True)
    Price               = models.IntegerField(max_length= 20)
    image               = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def get_url(self):
        return reverse('product_detail',args = [self.category.slug,self.slug])


    def __str__(self):
        return self.product_name
    
class VariationManager(models.Model):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_active= True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size',is_active= True)


# variation_category_choice = (
#         ('color','color'),
#         ('size','size'),

# )
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # variation_category = models.CharField(max_length=150,choices=variation_category_choice)
    # variation_value = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True, null=True,unique= True)
    size = models.CharField(max_length=50, blank=False, null=True,unique = True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = VariationManager()


    def __str__(self):
        return self.color


class ReviewRating(models.Model):
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     user = models.ForeignKey(Account, on_delete=models.CASCADE)
     subject = models.CharField(max_length=350,blank = True)
     review = models.TextField(max_length=500,blank = True)
     rating = models.FloatField(max_length=10)
     ip = models.CharField(max_length=50,blank = True)
     status = models.BooleanField(default=True)
     created_date = models.DateField(auto_now=False, auto_now_add=True)
     updated_date = models.DateField(auto_now=True, auto_now_add=False)

     def __str__(self):
        return self.subject
    