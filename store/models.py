from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField(null=False)
    quantity = models.SmallIntegerField(default=0)
    discount = models.FloatField(default=0.00)
    categories = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
