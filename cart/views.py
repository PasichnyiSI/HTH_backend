from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from .serializers import CartSerializer
from main.models import Product
from size.models import Size

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def add_item(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "Користувач не авторизований."}, status=status.HTTP_403_FORBIDDEN)

        product_id = request.data.get("product_id")
        size_id = request.data.get("size_id")
        quantity = int(request.data.get("quantity", 1))

        if not product_id:
            return Response({"detail": "Не вказано ID продукту."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
            size = Size.objects.get(id=size_id) if size_id else None
        except Product.DoesNotExist:
            return Response({"detail": "Продукт не знайдено."}, status=status.HTTP_404_NOT_FOUND)
        except Size.DoesNotExist:
            return Response({"detail": "Розмір не знайдено."}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def remove_item(self, request):
        user = request.user
        product_id = request.data.get("product_id")
        size_id = request.data.get("size_id")

        if not product_id:
            return Response({"detail": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Вибираємо кошик користувача без фільтрації по `is_active`
        user_cart = get_object_or_404(Cart, user=user)

        # Логіка видалення товару з кошика
        # Ти можеш також обробити видалення за розміром, якщо потрібно
        cart_item = user_cart.cartitem_set.filter(product_id=product_id, size_id=size_id).first()
        
        if cart_item:
            cart_item.delete()
            return Response({"detail": "Item removed from cart"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)
