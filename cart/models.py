from django.db import models
from main.models import Product
from size.models import Size
from django.contrib.auth import get_user_model

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Кошик для {self.user}"

    @property
    def items(self):
        return self.cartitem_set.all()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
