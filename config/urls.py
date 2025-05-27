from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("users/", include("users.urls", namespace="users")),
    path("products/", include("products.urls", namespace="products")),
    path("retail/", include("retail_chain.urls", namespace="retail")),

    path("schema/", views.SpectacularAPIView.as_view(), name="schema"),
    path("docs/", views.SpectacularSwaggerView.as_view(url_name="schema"), name="docs_swagger"),
    path("docs/redoc/", views.SpectacularRedocView.as_view(url_name="schema"), name="dosc_redoc"),
]
