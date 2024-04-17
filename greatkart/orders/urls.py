from . import views
from django.urls import path
urlpatterns = [
    path('Payment/',views.Payment,name = 'Payment'),
    path('Order/',views.Order,name = 'Order'),
    path('OrderProduct/',views.OrderProduct,name = 'OrderProduct'),
]