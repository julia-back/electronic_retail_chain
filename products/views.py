from rest_framework import generics
from .models import Product
from . import serializers


class ProductListAPIView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = serializers.ProductRetrieveSerializer
