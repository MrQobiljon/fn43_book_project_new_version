from django.urls import path

from .views import (all_books, books_by_category, book_detail, create_book, update_book, delete_book,
                    about, contact, books_by_favorite,
                    save_comment, update_comment, delete_comment)


urlpatterns = [
    path('', all_books, name='all_books'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/add/', create_book, name='add_book'),
    path('book/<int:book_id>/update/', update_book, name="book_update"),
    path('book/<int:book_id>/delete/', delete_book, name="book_delete"),

    path('category/<int:category_id>/', books_by_category, name='by_category'),
    path('books/', books_by_favorite, name='by_favorite'),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    path('add/comment/<int:book_id>/', save_comment, name='save_comment'),
    path('update/comment/<int:comment_id>/', update_comment, name='update_comment'),
    path('delete/comment/<int:comment_id>/', delete_comment, name='delete_comment'),
]