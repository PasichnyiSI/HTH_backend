from django.db import models
from main.models import Product
from size.models import Size
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Очікує'), ('completed', 'Завершене')],
        default='pending'
    )

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
    @property
    def items(self):
        return self.orderitem_set.all()
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


