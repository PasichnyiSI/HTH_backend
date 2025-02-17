from rest_framework import serializers
from .models import ProductRating
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']  # Тут ми вказуємо поле username, яке буде повертатися

class ProductRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Додаємо серіалізатор для користувача

    class Meta:
        model = ProductRating
        fields = ['product', 'user', 'rating', 'comment', 'photo']
