# cart/serializers.py
from rest_framework import serializers
from .models import Cart, CartItem
from main.serializers import ProductSerializer  # Для серіалізації продуктів
from size.serializers import SizeSerializer  # Для серіалізації розмірів

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    size_name = serializers.CharField(source="size.name", read_only=True)
    product_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "size", "size_name", "quantity", "product_price"]

    def get_product_price(self, obj):
        if obj.size:
            # Візьміть ціну для вибраного розміру
            product_size = obj.product.sizes.filter(size=obj.size).first()
            if product_size:
                return product_size.price
        # Якщо немає розміру, то використовуйте основну ціну
        return obj.product.price_per_sq_m

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items"]
