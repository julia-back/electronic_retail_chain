from rest_framework import generics
from .models import ChainNode, Contacts
from . import serializers


class ChainNodeListAPIView(generics.ListAPIView):
    """
    Класс представления списка объектов звена цепи.
    Поддерживает фильтрацию по полю страны связанного поля контакотов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeListSerializer
    filterset_fields = ["contacts__country"]


class ChainNodeRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс представления деталей объекта звена цепи.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ChainNodeCreateAPIView(generics.CreateAPIView):
    """
    Класс представления создания объекта звена цепи.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ChainNodeUpdateAPIView(generics.UpdateAPIView):
    """
    Класс представления обновления объекта звена цепи.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ChainNodeDestroyAPIView(generics.DestroyAPIView):
    """
    Класс представления удаления объекта звена цепи.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = ChainNode.objects.all()
    serializer_class = serializers.ChainNodeDetailSerializer


class ContactsListAPIView(generics.ListAPIView):
    """
    Класс представления списка объектов контактов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс представления деталей объекта контактов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsCreateAPIView(generics.CreateAPIView):
    """
    Класс представления создания объекта контактов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsUpdateAPIView(generics.UpdateAPIView):
    """
    Класс представления обновления объекта контактов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ContactsDestroyAPIView(generics.DestroyAPIView):
    """
    Класс представления удаления объекта контактов.
    Доступно активным пользователям, являющимися сотрудниками.
    """

    queryset = Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer
