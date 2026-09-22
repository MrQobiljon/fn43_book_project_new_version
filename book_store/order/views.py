from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from main.models import Book
from .models import Order, OrderProduct


def to_cart(request: HttpRequest, book_id: int, action: str):
    product = get_object_or_404(Book, pk=book_id)
    order, created = Order.objects.get_or_create(user=request.user, status="tan")
    order_product, created = OrderProduct.objects.get_or_create(order=order, product=product)

    if action == "add":
        order_product.quantity += 1
        order_product.save()
    elif action == "delete":
        if order_product.quantity == 0:
            order_product.delete()
        else:
            order_product.quantity -= 1
            order_product.save()

    page = request.META.get("HTTP_REFERER", "all_books")
    return redirect(page)