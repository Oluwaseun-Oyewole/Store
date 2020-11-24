from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'BUY/store.html', context)

def cart(request):
    # this is  for logged in user
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        # for unauthenticated user
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'BUY/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'BUY/checkout.html', context)

def updateItem(request):
    return JsonResponse('item was added', safe=False)