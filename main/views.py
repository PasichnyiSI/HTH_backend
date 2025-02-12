from .models import Product, Category
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, PopularProductsSerializer, NoveltiesProductsSerializer, BestProductsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PopularProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True, popular=True)
    serializer_class = PopularProductsSerializer

class NoveltiesProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True, novelties=True)
    serializer_class = NoveltiesProductsSerializer

class BestProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True, best=True)
    serializer_class = BestProductsSerializer

class CategoryDetailView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def list(self, request, *args, **kwargs):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


