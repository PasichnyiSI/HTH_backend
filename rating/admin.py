from django.contrib import admin
from .models import ProductRating

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'comment', 'created']
    list_filter = ['product', 'user']
