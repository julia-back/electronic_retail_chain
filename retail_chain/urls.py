from django.urls import path
from .apps import RetailChainConfig
from . import views

app_name = RetailChainConfig.name

urlpatterns = [
    path("chain_nodes/", views.ChainNodeListAPIView.as_view(), name="chain_node_list"),
    path("chain_node/<int:pk>/", views.ChainNodeRetrieveAPIView.as_view(), name="chain_node_retrieve"),
    path("chain_node/new/", views.ChainNodeCreateAPIView.as_view(), name="chain_node_create"),
    path("chain_node/<int:pk>/update/", views.ChainNodeUpdateAPIView.as_view(), name="chain_node_update"),
    path("chain_node/<int:pk>/delete/", views.ChainNodeDestroyAPIView.as_view(), name="chain_node_destroy"),

    path("contacts_list/", views.ContactsListAPIView.as_view(), name="contacts_list"),
    path("contacts/<int:pk>/", views.ContactsRetrieveAPIView.as_view(), name="contacts_retrieve"),
    path("contacts/new/", views.ContactsCreateAPIView.as_view(), name="contacts_create"),
    path("contacts/<int:pk>/update/", views.ContactsUpdateAPIView.as_view(), name="contacts_update"),
    path("contacts/<int:pk>/delete/", views.ContactsDestroyAPIView.as_view(), name="contacts_destroy"),
]
