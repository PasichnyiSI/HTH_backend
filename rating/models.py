from django.db import models
from django.contrib.auth import get_user_model
from main.models import Product

class ProductRating(models.Model):
    product = models.ForeignKey(Product, related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="ratings", on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # Рейтинг (0-5)
    comment = models.TextField(blank=True)  # Коментар (необов'язковий)
    photo = models.ImageField(upload_to='ratings_photos/', blank=True, null=True)  # Фото (необов'язкове)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Рейтинг {self.rating} для {self.product.name} від {self.user.username}"
