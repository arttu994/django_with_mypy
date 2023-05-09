from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from orders.models import Orders
from orders.serializers import OrdersSerializer


class OrdersView(ListCreateAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.all()


class OrdersRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.all()
