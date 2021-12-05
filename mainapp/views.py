from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from .models import Product, Category


class MainPage(ListView):
    template_name = 'index.html'


class ProductView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.select_related('category').all()
    # queryset = Product.objects.value_filter().select_related('category').all()


    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class CategoryView(ListView):
    model = Category
    template_name = 'categories.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукт'
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['objects'] = Product.objects.filter(category__pk=self.kwargs['pk'])

        return context
