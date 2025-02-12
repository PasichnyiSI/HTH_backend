from django.contrib import admin
from .models import Size, ProductSize

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'price')
    list_filter = ('product', 'size')
    search_fields = ('product__name', 'size__name')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Відображаємо лише поле name
    search_fields = ('name',)  # Пошук за іменем розміру

admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
