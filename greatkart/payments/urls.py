from . import views
from django.urls import path,include
urlpatterns = [
    path('paymentpage/',views.paymentpage,name = 'paymentpage'),
    path('paymentsuccess/',views.paymentsuccess,name = 'paymentsuccess'),
]