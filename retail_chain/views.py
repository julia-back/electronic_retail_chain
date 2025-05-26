from rest_framework import generics
from .models import ChainNode
from . import serializers


class ChainNodeListAPIView(generics.ListAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeListSerializer


class ChainNodeRetrieveAPIView(generics.RetrieveAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ChainNodeCreateAPIView(generics.CreateAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ChainNodeUpdateAPIView(generics.UpdateAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ChainNodeDestroyAPIView(generics.DestroyAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer
