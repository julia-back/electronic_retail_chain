from django.urls import path
from .apps import ProductsConfig
from . import views

app_name = ProductsConfig.name

urlpatterns = [
    path("products/", views.ProductListAPIView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductRetrieveAPIView.as_view(), name="product_retrieve"),
]
