from django.urls import path

from .views import to_cart

urlpatterns = [
    path('to/cart/<int:book_id>/<str:action>/', to_cart, name="to_cart"),
]