from rest_framework import serializers
from .models import CheckoutDetail

class CheckoutDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutDetail
        fields = '__all__'

    def validate_card_number(self, value):
        """Перевірка маскування картки"""
        if value and not value.isdigit():
            raise serializers.ValidationError("Номер картки повинен містити лише цифри.")
        return value[-4:]  # Зберігаємо тільки останні 4 цифри
