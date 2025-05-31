from rest_framework import generics
from .models import Product
from . import serializers


class ProductListAPIView(generics.ListAPIView):
    """
    Класс представления списка продуктов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс представления деталей продукта.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Product.objects.all()
    serializer_class = serializers.ProductRetrieveSerializer
