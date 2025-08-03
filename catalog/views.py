from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context=context)

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_card(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'catalog/product_card.html', context=context)
