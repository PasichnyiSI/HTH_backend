from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ProductRating, Product
from .serializers import ProductRatingSerializer

@api_view(['GET'])
def get_reviews(request, slug):
    """Отримання всіх відгуків для продукту за його slug."""
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return Response({"error": "Продукт не знайдено!"}, status=status.HTTP_404_NOT_FOUND)

    reviews = ProductRating.objects.filter(product=product)
    serializer = ProductRatingSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_product(request, slug):
    """Додавання або оновлення рейтингу та відгуку на продукт."""
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return Response({"error": "Продукт не знайдено!"}, status=status.HTTP_404_NOT_FOUND)

    try:
        rating_value = float(request.data.get('rating'))
        if not (0 <= rating_value <= 5):
            return Response({"error": "Рейтинг має бути в діапазоні від 0 до 5!"}, status=status.HTTP_400_BAD_REQUEST)
    except (TypeError, ValueError):
        return Response({"error": "Некоректне значення рейтингу!"}, status=status.HTTP_400_BAD_REQUEST)

    comment = request.data.get('comment', '').strip()
    photo = request.FILES.get('photo')

    user = request.user

    rating, created = ProductRating.objects.update_or_create(
        product=product, user=user,
        defaults={'rating': rating_value, 'comment': comment, 'photo': photo}
    )

    product.update_rating()  # Оновлюємо середній рейтинг продукту

    return Response({"message": "Рейтинг успішно додано!"}, status=status.HTTP_201_CREATED)
