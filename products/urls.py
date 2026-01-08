from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:pk>/', edit_product, name='edit_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
]
