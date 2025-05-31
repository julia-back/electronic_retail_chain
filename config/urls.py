from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views
from rest_framework.permissions import AllowAny


urlpatterns = [
    path("admin/", admin.site.urls),

    path("users/", include("users.urls", namespace="users")),
    path("products/", include("products.urls", namespace="products")),
    path("retail/", include("retail_chain.urls", namespace="retail")),

    path("schema/", views.SpectacularAPIView.as_view(permission_classes=[AllowAny]), name="schema"),
    path("docs/", views.SpectacularSwaggerView.as_view(permission_classes=[AllowAny], url_name="schema"), name="docs_swagger"),
    path("docs/redoc/", views.SpectacularRedocView.as_view(permission_classes=[AllowAny], url_name="schema"), name="dosc_redoc"),
]
