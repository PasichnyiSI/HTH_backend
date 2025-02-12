from rest_framework import serializers
from .models import Size, ProductSize
from main.models import Product

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class ProductSizeSerializer(serializers.ModelSerializer):
    size = SizeSerializer() 

    class Meta:
        model = ProductSize
        fields = ['size', 'price']