from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CheckoutDetail
from .serializers import CheckoutDetailSerializer

class CheckoutDetailViewSet(viewsets.ModelViewSet):
    queryset = CheckoutDetail.objects.all()
    serializer_class = CheckoutDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Прив’язуємо checkout до користувача та замовлення"""
        serializer.save(user=self.request.user)
