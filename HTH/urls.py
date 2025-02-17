from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views
from size.views import SizeViewSet, ProductSizeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', main_views.ProductViewSet, basename='products')
router.register(r'categories', main_views.CategoryViewSet, basename='categories')
router.register(r'popular-products', main_views.PopularProductsViewSet, basename='popular-products')
router.register(r'novelties-products', main_views.NoveltiesProductsViewSet, basename='novelties-products')
router.register(r'best-products', main_views.BestProductsViewSet, basename='best-products')
router.register(r'category_products', main_views.CategoryDetailView, basename='category_products')
router.register(r'size', SizeViewSet, basename='size')
router.register(r'product-size', ProductSizeViewSet, basename='product-size')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('api/router/', include(router.urls)),
    path('users/', include("users.urls")),
    path('cart/', include("cart.urls")),
    path('size/', include("size.urls")),
    path('rating/', include("rating.urls")),
    path('wishlist/', include("wishlist.urls")),
    path('comparisonlist/', include("comparisonlist.urls")),
    path('orders/', include("orders.urls")),
    path('checkout/', include("checkout.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
