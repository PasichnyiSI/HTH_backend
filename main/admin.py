from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price_per_sq_m', 'available', 'created', 'updated', 'discount']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price_per_sq_m', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}

