from django.shortcuts import render

# Create your views here.
def paymentpage(request):
    return render(request,'payment.html')
def paymentsuccess(request):
    return render(request,'paymentsuccess.html')