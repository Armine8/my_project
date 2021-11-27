from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product


class ProductView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()