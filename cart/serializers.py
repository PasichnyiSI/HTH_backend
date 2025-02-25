# cart/serializers.py
from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    size_name = serializers.CharField(source="size.name", read_only=True)
    product_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "size", "size_name", "quantity", "product_price"]

    def get_product_price(self, obj):
        if obj.size:
            product_size = obj.product.sizes.filter(size=obj.size).first()
            if product_size:
                price = product_size.price
        else:
            price = obj.product.price_per_sq_m

        # Якщо є знижка, застосовуємо її
        if obj.product.discount and obj.product.discount > 0:
            discounted_price = price * (1 - obj.product.discount / 100)
            return round(discounted_price)

        return round(price)

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items"]
