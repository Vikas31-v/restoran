import razorpay
from django.shortcuts import render
from cart.models import Cart
from django.conf import settings
from django.contrib.auth.models import User
from order.models import Order,OrderItem
from accounts.models import Address
# Create your views here.

def checkout(request):
    return render(request,'payment/checkout.html')


def Proceed_to_payment(request):
    RAZORPAY_KEY_ID = settings.RAZORPAY_KEY_ID
    RAZORPAY_KEY_SECRET = settings.RAZORPAY_KEY_SECRET
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET ))
    user = User.objects.get(username = request.user)
    cart_item=Cart.objects.filter(user =request.user)
    total=0
    for item in cart_item:
        total += item.product.price * item.quantity
    order = Order.objects.filter(user = user).filter(status='CREATED')
    if not order:
        Order.objects.create(
            user = user,
            # status = 'CREATED',
            total  = total,
            shipping_address = Address.objects.get(id=int(request.session['address_id'])),
            shipping_charges = 100
        )
    for item in cart_item:
        total += item.product.price_inclusive * item.quantity
        OrderItem.objects.create(
            order_id=order,
            product=item.order,
            dish=item.dish,
            quantity = item.quantity,
            price = item.price_at_time_of_order )
    order.total = total
    order.save()
        
    data = { "amount": int(total), "currency": "INR", "receipt": str(order.order_uuid)}
    razor_pay_order = client.order.create(data=data)
    context = {
        'order':razor_pay_order,
        'data':data,
    }
    return render(request,'payment/checkout.html',context)