from rest_framework import generics
from .models import ChainNode, Contacts
from . import serializers


class ChainNodeListAPIView(generics.ListAPIView):

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeListSerializer
    filterset_fields = ["contacts__country"]


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


class ContactsListAPIView(generics.ListAPIView):

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsCreateAPIView(generics.CreateAPIView):

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsUpdateAPIView(generics.UpdateAPIView):

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsDestroyAPIView(generics.DestroyAPIView):

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer
