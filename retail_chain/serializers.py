from rest_framework import serializers
from .models import ChainNode, Contacts
from .validators import FactoryNotHaveSupplierValidator, FactoryNotHavePaymentArrearsValidator


class ChainNodeListSerializer(serializers.ModelSerializer):
    """Класс сериализатора для списка объектов звена цепи."""

    class Meta:
        model = ChainNode
        fields = ["id", "name", "node_type"]


class ChainNodeDetailSerializer(serializers.ModelSerializer):
    """Класс сериализатора для получения деталей, создания, обновления, удаления объекта звена цепи."""

    class Meta:
        model = ChainNode
        fields = "__all__"
        read_only_fields = ["node_level", "payment_arrears"]
        validators = [
            FactoryNotHaveSupplierValidator(),
            FactoryNotHavePaymentArrearsValidator()
        ]


class ContactsSerializer(serializers.ModelSerializer):
    """Класс сериализатора объекта контактов."""

    class Meta:
        model = Contacts
        fields = "__all__"
