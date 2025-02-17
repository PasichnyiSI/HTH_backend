from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Comparisonlist, ComparisonlistItem
from .serializers import ComparisonlistSerializer
from main.models import Product

class ComparisonlistViewSet(viewsets.ModelViewSet):
    queryset = Comparisonlist.objects.all()
    serializer_class = ComparisonlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comparisonlist.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def add_item(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "Користувач не авторизований."}, status=status.HTTP_403_FORBIDDEN)

        product_id = request.data.get("product_id")

        if not product_id:
            return Response({"detail": "Не вказано ID продукту."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Продукт не знайдено."}, status=status.HTTP_404_NOT_FOUND)

        comparisonlist, created = Comparisonlist.objects.get_or_create(user=user)
        comparisonlist_item, created = ComparisonlistItem.objects.get_or_create(comparisonlist=comparisonlist, product=product)

        comparisonlist_item.save()
        serializer = ComparisonlistSerializer(comparisonlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def remove_item(self, request):
        user = request.user
        product_id = request.data.get("product_id")

        if not product_id:
            return Response({"detail": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Вибираємо кошик користувача без фільтрації по `is_active`
        user_comparisonlist = get_object_or_404(Comparisonlist, user=user)

        # Логіка видалення товару з кошика
        # Ти можеш також обробити видалення за розміром, якщо потрібно
        comparisonlist_item = user_comparisonlist.comparisonlistitem_set.filter(product_id=product_id).first()
        
        if comparisonlist_item:
            comparisonlist_item.delete()
            return Response({"detail": "Item removed from comparisonlist"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Item not found in comparisonlist"}, status=status.HTTP_404_NOT_FOUND)
