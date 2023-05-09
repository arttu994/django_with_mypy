from django.urls import path

from orders.views import OrdersView, OrdersRetriveUpdateDestroyView


urlpatterns = [
    path("", OrdersView.as_view(), name="order_view"),
    path(
        "<int:pk>/",
        OrdersRetriveUpdateDestroyView.as_view(),
        name="order_get_update_delete",
    ),
]
