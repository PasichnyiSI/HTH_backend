from django.db import models
from django.urls import reverse
from django.db.models import Avg, Count

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price_per_sq_m = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ціна за 1 м²")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    popular = models.BooleanField(default=False)
    novelties = models.BooleanField(default=False)
    best = models.BooleanField(default=False)

    # Нові поля для збереження середнього рейтингу та кількості оцінок
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def update_rating(self):
        """Оновлює середній рейтинг та кількість оцінок для продукту"""
        from django.db.models import Avg, Count  # Імпортуємо тут, щоб уникнути циклічного імпорту

        stats = self.ratings.aggregate(avg_rating=Avg("rating"), total=Count("rating"))
        
        self.average_rating = round(stats["avg_rating"], 1) if stats["avg_rating"] is not None else 0.0
        self.rating_count = stats["total"] if stats["total"] is not None else 0
        
        self.save(update_fields=["average_rating", "rating_count"])  # Оновлюємо тільки ці поля

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.slug])
    