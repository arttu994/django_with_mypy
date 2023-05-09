from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from store.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "parent", "children"]
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "quantity",
            "discount",
            "categories",
        ]
        extra_kwargs = {"id": {"read_only": True}}
