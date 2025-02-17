from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CheckoutDetailViewSet

router = DefaultRouter()
router.register(r'checkout', CheckoutDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
