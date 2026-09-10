from django.contrib import admin

from .models import Category, Book, Comment

admin.site.register([Category, Book, Comment])