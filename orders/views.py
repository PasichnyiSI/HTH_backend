from rest_framework import viewsets, permissions, status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import CartItem, Cart


def send_order_confirmation(order):
    subject = f"Нове замовлення #{order.id}"
    message = f"Замовлення від користувача: {order.user.username}. Загальна сума: {order.total_price}."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order.email])


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email є обов\'язковим.'}, status=status.HTTP_400_BAD_REQUEST)
        # Знаходимо активну корзину користувача
        try:
            cart = Cart.objects.get(user=user, is_active=True)
        except Cart.DoesNotExist:
            return Response({'error': 'Кошик не знайдено'}, status=status.HTTP_400_BAD_REQUEST)

        # Фільтруємо елементи корзини за корзиною, а не за користувачем
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({'error': 'Корзина порожня'}, status=status.HTTP_400_BAD_REQUEST)
        
        total_price = sum(
            (item.product.sizes.filter(size=item.size).first().price if item.size else item.product.price_per_sq_m) * item.quantity
            for item in cart_items
        )

        # Створюємо замовлення
        order = Order.objects.create(user=user, email=email, total_price=total_price)

        # Додаємо елементи до замовлення
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                size=item.size,
                quantity=item.quantity
            )
        # Очищаємо корзину після оформлення замовлення
        send_order_confirmation(order)
        cart_items.delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)