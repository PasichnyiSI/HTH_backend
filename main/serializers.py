from rest_framework import serializers
from .models import Product, Category
from size.serializers import ProductSizeSerializer
from django.db.models import Avg, Count


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    sizes = ProductSizeSerializer(many=True, read_only=True)
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'image', 'description', 'price_per_sq_m', 
                  'available', 'discount', 'sizes', 'average_rating', 'rating_count']
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'products']

class PopularProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name', 'slug', 'image', 'description', 'price_per_sq_m', 'available', 'discount', 'popular']

class NoveltiesProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name', 'slug', 'image', 'description', 'price_per_sq_m', 'available', 'discount', 'novelties']

class BestProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name', 'slug', 'image', 'description', 'price_per_sq_m', 'available', 'discount', 'best']
