from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name"]


class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
