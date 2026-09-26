from django.urls import path

from .views import to_cart, cart, delete_from_cart, clear_cart

urlpatterns = [
    path('to/cart/<int:book_id>/<str:action>/', to_cart, name="to_cart"),
    path('cart/', cart, name='cart'),
    path('delete/order/product/<int:order_product_id>/', delete_from_cart, name='delete_from_cart'),
    path('clear/cart/', clear_cart, name='clear_cart'),
]