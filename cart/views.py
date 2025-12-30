from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import *
from .models import *

# Create your views here.

def cart(request, total = 0, quantity = 0, cart_items = None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = Items.objects.filter(cart = cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total' : grand_total,
    } 
    return render(request, 'store/cart.html', context )

def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def add_cart(request,product_id):
    product = Product.objects.get(id= product_id )
    product_variation = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product = product, variation_catgory__iexact = key, variation_value__iexact = value)
                product_variation.append(variation)
            except:
                pass



    try:
        cart_obj = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart_obj = Cart.objects.create(cart_id = _cart_id(request))
        cart_obj.save()


    item_exists = Items.objects.filter(product = product, cart = cart_obj).exists()
    if item_exists:
        cart_item = Items.objects.filter(product = product, cart = cart_obj)
        
        exist_variation_list = []
        id = []
        for item in cart_item:
            exist_variation = item.variation.all()
            exist_variation_list.append(list(exist_variation))
            id.append(item.id)
        
        if product_variation in exist_variation_list:
            index = exist_variation_list.index(product_variation)
            item_id = id[index]
            item = Items.objects.get(product = product, id = item_id)
            item.quantity +=1 
            item.save()
            # return redirect('cart')
        else:
            item = Items.objects.create(product = product, cart = cart, quantity = 1) 
            if len(product_variation) > 0:
                item.variation.clear()
                item.variation.add(*product_variation)
            item.save()
    else:
        cart_item = Items.objects.create(
            product = product,
            cart = cart_obj,
            quantity = 1,
        )
        if len(product_variation) > 0:
            cart_item.variation.clear()
            cart_item.variation.add(*product_variation)
        cart_item.save()
    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id )
    cart_item = Items.objects.get(product = product, cart = cart )
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id )
    cart_item = Items.objects.get(product = product, cart = cart )
    cart_item.delete()
    return redirect('cart')