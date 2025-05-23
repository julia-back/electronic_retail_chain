from rest_framework import generics
from .models import ChainNode
from . import serializers


class ChainNodeListAPIView(generics.ListAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeListSerializer
    permission_classes = []


class ChainNodeRetrieveAPIView(generics.RetrieveAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer
    permission_classes = []


class ChainNodeCreateAPIView(generics.CreateAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer
    permission_classes = []


class ChainNodeUpdateAPIView(generics.UpdateAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer
    permission_classes = []


class ChainNodeDestroyAPIView(generics.DestroyAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer
    permission_classes = []
