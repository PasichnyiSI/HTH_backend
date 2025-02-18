from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    size_name = serializers.CharField(source="size.name", read_only=True)
    product_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_product_price(self, obj):
        if obj.size:
            product_size = obj.product.sizes.filter(size=obj.size).first()
            if product_size:
                price = product_size.price
        else:
            price = obj.product.price_per_sq_m

        if obj.product.discount and obj.product.discount > 0:
            discounted_price = price * (1 - obj.product.discount / 100)
            return round(discounted_price)

        return round(price)

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=0, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order
