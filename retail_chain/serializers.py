from rest_framework import serializers
from .models import ChainNode


class ChainNodeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChainNode
        fields = ["id", "name"]


class ChainNodeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChainNode
        fields = "__all__"
        read_only_fields = ["payment_arrears"]
