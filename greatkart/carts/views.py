from django.shortcuts import render, redirect,get_object_or_404
from carts.models import Cart
from .models import cartItem
from store.models import Variation
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=_cart_id(request)
            )

        try:
            cart_item = cartItem.objects.get(product=product, user=current_user)
            cart_item.cart_quantity += 1
            cart_item.save()
        except cartItem.DoesNotExist:
            cart_item = cartItem.objects.create(
                product=product,
                cart_quantity=1,
                user=current_user,
            )
            cart_item.save()
        return redirect('cart')
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=_cart_id(request)
            )

        try:
            cart_item = cartItem.objects.get(product=product, cart=cart)
            cart_item.cart_quantity += 1
            cart_item.save()
        except cartItem.DoesNotExist:
            cart_item = cartItem.objects.create(
                product=product,
                cart_quantity=1,
                cart=cart,
            )
            cart_item.save()
        return redirect('cart')

def cart(request,total = 0,quantity = 0, cart_items = None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = cartItem.objects.filter(user = request.user,is_active = True)
        else: 
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_items = cartItem.objects.filter(cart = cart,is_active = True)
        for cart_item in  cart_items:
            total += (cart_item.product.Price * cart_item.cart_quantity)
            quantity += cart_item.cart_quantity

        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total' : total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax':tax,
        'grand_total': grand_total,

    }
    return render(request, 'cart.html',context)

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id = product_id)
        cart_item = cartItem.objects.get(product = product, user = request.user)
        if cart_item.cart_quantity > 1:
            cart_item.cart_quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    else:
        product = get_object_or_404(Product, id = product_id)
        cart_item = cartItem.objects.get(product = product, cart = cart)
        if cart_item.cart_quantity > 1:
            cart_item.cart_quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        product = get_object_or_404(Product, id = product_id)
        cart_item = cartItem.objects.get(product = product, user = request.user)
        cart_item.delete()
        return redirect('cart')
    else:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        product = get_object_or_404(Product, id = product_id)
        cart_item = cartItem.objects.get(product = product, cart = cart)
        cart_item.delete()
        return redirect('cart')

@login_required(login_url= 'login')
def placeorder(request,total = 0,quantity = 0, cart_items = None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = cartItem.objects.filter(user = request.user,is_active = True)
        for cart_item in  cart_items:
            total += (cart_item.product.Price * cart_item.cart_quantity)
            quantity += cart_item.cart_quantity

        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total' : total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax':tax,
        'grand_total': grand_total,

    }
    return render(request, 'place-order.html',context)


# from django.shortcuts import render,redirect
# from carts.models import Cart,cartItem
# from store.models import Product
# # Create your views here.
# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart


# def add_cart(request,product_id):
#     product = Product.objects.get(id = product_id)
#     try:
#         cart = Cart.objects.get(cart_id = _cart_id(request))
#     except cart.DoesnotExist:
#         cart = Cart.objects.create(
#             cart_id = _cart_id(request)
#         )
#     cart.save()

#     try:
#         cart_item = cartItem.objects.get(product = product , cart = cart)
#         cart_item.quantity += 1
#         cart_item.save()
#     except cartItem.DoesnotExist:
#         cart_item = cartItem.objects.create(
#             product = product,
#             quantity = 1,
#             cart = cart,
#         )
#         cart_item.save()
#         return redirect('cart')



# def cart(request):
#     return render(request,'cart.html')


