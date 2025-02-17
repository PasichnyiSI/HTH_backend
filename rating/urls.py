from django.urls import path
from . import views

urlpatterns = [
    path('ratings/<slug:slug>/rate/', views.rate_product, name='rate_product'),
    path('ratings/<slug:slug>/', views.get_reviews, name='get_reviews'),
]
