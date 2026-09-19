import json

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_POST
from django.db.models import Exists, OuterRef
from django.core.paginator import Paginator


from .models import Category, Book, Comment, Favorite
from .forms import BookForm, CommentForm


def save_favorite_book(request):
    if request.user.is_authenticated:
        favorite_id = request.GET.get('favorite')
        book = get_object_or_404(Book, pk=favorite_id)
        obj, created = Favorite.objects.get_or_create(book=book, user=request.user)
        if not created:
            obj.delete()
    else:
        messages.warning(request, "Tanlash uchun login qiling")
        return redirect('login')


def all_books(request: HttpRequest):
    if request.GET.get("favorite"):
        save_favorite_book(request)

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(
            book=OuterRef("pk"),
            user=request.user
        )

        books = Book.objects.annotate(
            is_favorite=Exists(favorite)
        )
    else:
        books = Book.objects.filter(published=True)

    p = Paginator(books, 6)
    page = p.page(request.GET.get("page", 1))

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'books': page.object_list,
        "page": page,
        "title": "Asosiy sahifa"
    }
    return render(request, 'main/all_books.html', context)


def books_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.GET.get("favorite"):
        save_favorite_book(request)

    favorite = Favorite.objects.filter(
        book=OuterRef("pk"),
        user=request.user
    )

    books = Book.objects.annotate(
        is_favorite=Exists(favorite)
    ).filter(category_id=category_id, published=True)

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'books': books,
        'title': category.name
    }
    return render(request, 'main/all_books.html', context)


@login_required()
def books_by_favorite(request):
    categories = Category.objects.all()

    if request.GET.get("favorite"):
        save_favorite_book(request)

    favorite = Favorite.objects.filter(
        book=OuterRef("pk"),
        user=request.user
    )

    books = Book.objects.annotate(
        is_favorite=Exists(favorite)
    ).filter(is_favorite=True, published=True)

    context = {
        'categories': categories,
        'books': books,
    }
    return render(request, 'main/all_books.html', context)


@permission_required('main.view_book')
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id, published=True)
    comments = Comment.objects.filter(book_id=book_id).order_by('-created')
    context = {
        "book": book,
        "comments": comments,
        "title": book.title,
        "form": CommentForm()
    }
    return render(request, "main/book_detail.html", context)


@permission_required('main.add_book')
@login_required(login_url='login')
def create_book(request):
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, "Kitob muvaffaqiyatli qo'shildi!")
            return redirect("book_detail", book_id=book.id)
    else:
        form = BookForm()
    context = {
        "form": form,
        "title": "Kitob qo'shish"
    }
    return render(request, "main/book-form.html", context)


@permission_required('main.change_book')
@login_required(login_url='login')
def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqiyatli o'zgartirildi!")
            return redirect("book_detail", book_id=book.id)
    else:
        form = BookForm(instance=book)
    context = {
        "form": form,
        "title": "O'zgartirilimoqda: " + book.title
    }
    return render(request, "main/book-form.html", context)


@permission_required('main.delete_book', login_url='login')
@login_required(login_url="login")
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Mufavvaqiyatli o'chirildi!")
        return redirect('all_books')
    else:
        return render(request, "main/book_confim_delete.html", {"book": book, "title": "O'chirilmoqda"})


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


@login_required(login_url='all_books')
def save_comment(request, book_id):
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            book = get_object_or_404(Book, pk=book_id, published=True)
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            messages.success(request, "Commentariya qo'shildi!!!")
            return redirect('book_detail', book_id=book_id)
    else:
        return redirect('all_books')


@require_POST
def update_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)

    except Comment.DoesNotExist:

        return JsonResponse(
            {
                "error": "Comment topilmadi!"
            },
            status=404
        )

    try:

        data = json.loads(request.body)

    except json.JSONDecodeError:

        return JsonResponse(
            {
                "error": "Noto'g'ri ma'lumot!"
            },
            status=400
        )

    text = data.get("text", "").strip()

    if not text:
        return JsonResponse(
            {
                "error": "Comment bo'sh bo'lishi mumkin emas!"
            },
            status=400
        )

    comment.text = text
    comment.save()

    return JsonResponse(
        {
            "success": True,
            "text": comment.text
        }
    )


@login_required(login_url='all_books')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        book_id = comment.book.id
        if request.method == 'POST':
            comment.delete()
            return redirect('book_detail', book_id=book_id)
        else:
            return render(request, "main/confirm_delete.html", {"comment": comment})
    else:
        return redirect('home')
