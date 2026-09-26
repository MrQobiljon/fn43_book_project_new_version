from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from main.models import Book
from .models import Order, OrderProduct


@login_required
def to_cart(request: HttpRequest, book_id: int, action: str):
    product = get_object_or_404(Book, pk=book_id)
    order, created = Order.objects.get_or_create(user=request.user, status="tan")
    order_product, created = OrderProduct.objects.get_or_create(order=order, product=product)

    if action == "add":
        order_product.quantity += 1
        order_product.save()
    elif action == "delete":
        if order_product.quantity <= 1:
            order_product.delete()
        else:
            order_product.quantity -= 1
            order_product.save()

    page = request.META.get("HTTP_REFERER", "all_books")
    return redirect(page)


@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, status="tan")
    order_products = order.products.all()
    context = {
        "order_products": order_products,
        "order": order
    }
    return render(request, "order/cart.html", context)


@login_required
def delete_from_cart(request, order_product_id: int):
    order_product = get_object_or_404(OrderProduct, pk=order_product_id)
    order_product.delete()
    return redirect('cart')


@login_required
def clear_cart(request):
    order, created = Order.objects.get_or_create(user=request.user, status="tan")
    order_products = order.products.all()
    order_products.delete()
    return redirect('cart')