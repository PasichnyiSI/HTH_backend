from rest_framework import serializers
from .models import Comparisonlist, ComparisonlistItem
from main.serializers import ProductSerializer 

class ComparisonlistItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = ComparisonlistItem
        fields = ["id", "product", "product_name", "product_price", "product_image"]

    def get_product_price(self, obj):
        price = obj.product.price_per_sq_m
        if obj.product.discount and obj.product.discount > 0:
            discounted_price = price * (1 - obj.product.discount / 100)
            return round(discounted_price)

        return round(price)
    
    def get_product_image(self, obj):
        request = self.context.get("request")  # Отримуємо request для побудови абсолютного URL
        if obj.product.image:
            return request.build_absolute_uri(obj.product.image.url) if request else obj.product.image.url
        return None  # Якщо зображення немає

class ComparisonlistSerializer(serializers.ModelSerializer):
    items = ComparisonlistItemSerializer(many=True, read_only=True)
    class Meta:
        model = Comparisonlist
        fields = '__all__'
