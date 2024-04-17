from django.contrib import admin
from .models import Product,Variation,ReviewRating
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('product_name',)
    }
    list_display = ['product_name','Price','stock','is_available','modified_date']
    list_filter = ['product_name','category','modified_date']

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product','color','size','is_active','created_date']
    list_filter = ['product','is_active','created_date']
    list_editable = ['is_active',]
    
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['product','user','review','rating','ip','status']
    list_filter = ['product','status','updated_date']
    list_editable = ['status',]


admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating,ReviewRatingAdmin)
