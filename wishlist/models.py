from django.db import models
from main.models import Product
from django.contrib.auth import get_user_model

class Wishlist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Список бажаного для {self.user}"
    
    @property
    def items(self):
        return self.wishlistitem_set.all()
        

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}"


