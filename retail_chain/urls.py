from django.urls import path
from .apps import RetailChainConfig
from . import views

app_name = RetailChainConfig.name

urlpatterns = [
    path("chain_nodes/", views.ChainNodeListAPIView.as_view(), name="chain_node_list"),
    path("chain_node/<int:pk>/", views.ChainNodeRetrieveAPIView.as_view(), name="chain_node_retrieve"),
    path("chain_node/new/", views.ChainNodeCreateAPIView.as_view(), name="chain_node_create"),
    path("chain_node/<int:pk>/", views.ChainNodeUpdateAPIView.as_view(), name="chain_node_update"),
    path("chain_node/<int:pk>/", views.ChainNodeDestroyAPIView.as_view(), name="chain_node_destroy"),
]
