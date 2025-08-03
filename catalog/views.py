from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCardDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_card.html'
    context_object_name = 'product'
