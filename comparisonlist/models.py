from django.db import models
from main.models import Product
from django.contrib.auth import get_user_model

class Comparisonlist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Список бажаного для {self.user}"
    
    @property
    def items(self):
        return self.comparisonlistitem_set.all()
        

class ComparisonlistItem(models.Model):
    comparisonlist = models.ForeignKey(Comparisonlist, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}"


