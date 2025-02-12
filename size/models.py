from django.db import models
from main.models import Product  # Імпортуємо модель продукту

class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Наприклад, "70x190", "80x200"
    
    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.size.name}"

    class Meta:
        unique_together = ('product', 'size')
