from django.db import models
from main.models import Product
from size.models import Size
from django.contrib.auth import get_user_model

class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Очікує підтвердження'),
        ('processing', 'В обробці'),
        ('completed', 'Завершено'),
        ('canceled', 'Скасовано'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, null=False)


    def __str__(self):
        return f"Замовлення {self.id} - {self.user.username} ({self.status})"
    
    @property
    def items(self):
        return self.orderitem_set.all()
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} х {self.quantity}"
