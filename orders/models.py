from django.db import models

from authentication.models import User
from store.models import Product


class Orders(models.Model):
    order_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.order_date}, {self.user}, {self.product}"
