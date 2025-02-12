from django.urls import path
from . import views
from .views import CategoryDetailView, ProductViewSet


app_name = 'main'

urlpatterns = [
    # path('api/router/products/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('api/router/product/<slug:slug>/', ProductViewSet.as_view(), name='product-detail'),

]
