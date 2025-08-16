from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView, DetailView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from .forms import ProductForm
from .models import Product

class ProductUnpublishedView(LoginRequiredMixin, View):
    model = Product

    def post(self, request, product_id):
        product = get_object_or_404(Product, product_id)
        if not self.request.user.has_perm('catalog.can_unpublished_product'):
            return HttpResponseForbidden('У вас нет прав для отмены публикации продукта')
        product.is_published = False
        product.save()
        redirect('catalog:product_card', pk=product_id)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCardDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_card.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    # def post(self, request, form, product_id=id):
    #     product = get_object_or_404(Product, product_id)
    #     if not self.request.user.has_perm('catalog.can_delete_product'):
    #         return HttpResponseForbidden('У вас нет прав для удаления продукта')
    #     else:
    #         form.instance.user = self.request.user
    #         return super().form_valid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
