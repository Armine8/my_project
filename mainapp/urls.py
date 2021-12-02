from django.urls import path

from .views import ProductView, CategoryView


urlpatterns = [
    path('', ProductView.as_view(),name = 'product'),
    path('categories/<int:pk>', CategoryView.as_view(), name='category')
]
