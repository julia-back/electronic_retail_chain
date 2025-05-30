from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """Класс сериализатора для списка продуктов, отображает только id и назване."""

    class Meta:
        model = Product
        fields = ["id", "name"]


class ProductRetrieveSerializer(serializers.ModelSerializer):
    """Класс сериализатора для получения деталей продукта."""

    class Meta:
        model = Product
        fields = "__all__"
