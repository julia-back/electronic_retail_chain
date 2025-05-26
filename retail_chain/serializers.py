from rest_framework import serializers
from .models import ChainNode
from .validators import FactoryNotHaveSupplierValidator, FactoryNotHavePaymentArrearsValidator


class ChainNodeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChainNode
        fields = ["id", "name", "node_type"]


class ChainNodeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChainNode
        fields = "__all__"
        read_only_fields = ["node_level", "payment_arrears"]
        validators = [
            FactoryNotHaveSupplierValidator(),
            FactoryNotHavePaymentArrearsValidator()
        ]
