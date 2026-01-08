from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    # Auth
    path('auth/register/', RegisterAPI.as_view(), name='api-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='api-token-refresh'),

    # Products
    path('products/', ProductListAPI.as_view(), name='api-product-list'),
    path('products/<int:pk>/', ProductDetailAPI.as_view(), name='api-product-detail'),
    path('products/create/', ProductCreateAPI.as_view(), name='api-product-create'),
    path('products/<int:pk>/update/', ProductUpdateAPI.as_view(), name='api-product-update'),
    path('products/<int:pk>/delete/', ProductDeleteAPI.as_view(), name='api-product-delete'),
]
