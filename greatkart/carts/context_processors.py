from .models import Cart,cartItem
from .views import _cart_id
from django.contrib.auth import authenticate

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id = _cart_id(request))
            if request.user.is_authenticated:
                cart_items = cartItem.objects.all().filter(user = request.user)
            else:
                cart_items = cartItem.objects.all().filter(cart = cart[:1])
            for cart_item in cart_items:
                cart_count +=  cart_item.cart_quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
            