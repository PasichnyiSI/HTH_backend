from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import CartItem, Cart

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        # Знаходимо активну корзину користувача
        try:
            cart = Cart.objects.get(user=user, is_active=True)
        except Cart.DoesNotExist:
            return Response({'error': 'Кошик не знайдено'}, status=status.HTTP_400_BAD_REQUEST)

        # Фільтруємо елементи корзини за корзиною, а не за користувачем
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({'error': 'Корзина порожня'}, status=status.HTTP_400_BAD_REQUEST)

        # Створюємо замовлення
        order = Order.objects.create(user=user)

        # Додаємо елементи до замовлення
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Очищаємо корзину після оформлення замовлення
        cart_items.delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
