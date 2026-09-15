from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def count_books(self):
        return self.book_set.filter(published=True).count()


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kitob nomi")
    introduction = models.TextField(null=True, blank=True, verbose_name="Muqaddima")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Rasmi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


class Comment(models.Model):
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text


class Favorite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.book.title}"

    class Meta:
        unique_together = [['book', 'user']]