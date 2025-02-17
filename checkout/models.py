from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order

class CheckoutDetail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    PAYMENT_METHODS = [
        ('card', 'Credit/Debit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash on Delivery'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)

    card_number = models.CharField(max_length=16, blank=True, null=True)  # Для збереження маскованого номера картки
    expiration_date = models.CharField(max_length=5, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Checkout for Order {self.order.id}"
