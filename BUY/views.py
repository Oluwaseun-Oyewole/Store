from django.shortcuts import render
from .models import *

def store(request):

    context = {}
    return render(request, 'BUY/store.html', context)

def cart(request):
    context = {}
    return render(request, 'BUY/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'BUY/checkout.html', context)