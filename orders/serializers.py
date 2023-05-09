from rest_framework import serializers

from orders.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
        extra_kwargs = {"order_date": {"read_only": True}}
