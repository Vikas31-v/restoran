from django.shortcuts import render, redirect
from .models import *


def remove_item_from_cart(request,id):
    Cart.objects.get(id = id).delete()
    #request.session['cart_item_count'] -=1
    return redirect('cart_view')

