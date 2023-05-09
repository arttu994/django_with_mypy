from django.urls import path

from store.views import (
    CategoryView,
    CategoryRetriveUpdateDestroyView,
    ProductView,
    ProductRetriveUpdateDestroyView,
)


urlpatterns = [
    path("category/", CategoryView.as_view(), name="category_view"),
    path(
        "category/<int:pk>/",
        CategoryRetriveUpdateDestroyView.as_view(),
        name="category_get_update_delete",
    ),
    path("product/", ProductView.as_view(), name="product_view"),
    path(
        "product/<int:pk>/",
        ProductRetriveUpdateDestroyView.as_view(),
        name="product_get_update_delete",
    ),
]
