from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComparisonlistViewSet

router = DefaultRouter()
router.register(r'comparisonlist', ComparisonlistViewSet, basename='comparisonlist')

urlpatterns = [
    path('', include(router.urls)),
]
