from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Book, Comment, Favorite

admin.site.site_title = "Liberty"
admin.site.site_header = "Admin Panel"
admin.site.index_title = "Admin Sahifasi"
# admin.site.login_template = "admin/login.html"

admin.site.register([Category, Favorite])


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('text', 'user')
    extra = 0
    can_delete = False


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'get_introduction', 'price', 'created', 'category', 'published', 'get_image', 'my_test')
    list_display_links = ('title',)
    list_editable = ('published', 'category', 'price')
    list_filter = ('category', 'published')
    search_fields = ("title", "introduction", "category__name", "price")
    inlines = [
        CommentInline
    ]
    # fields = [
    #     ('title', 'introduction'),
    #     ('price', 'image'),
    #     ('category', 'published'),
    # ]
    # fieldsets = [
    #     (
    #         "Asosiy",
    #         {
    #             'fields': ['title', 'introduction'],
    #             "classes": ["collapse"],
    #         }
    #     ),
    #     (
    #         "Narxlari",
    #         {
    #             "fields": ['price'],
    #             "classes": ["collapse"],
    #         }
    #     ),
    #     (
    #         "Media",
    #         {
    #             "fields": ["image"],
    #             "classes": ["collapse"],
    #         }
    #     ),
    #     (
    #         "Tanlov",
    #         {
    #             "fields": ["category", "published"],
    #             "classes": ["collapse"],
    #         }
    #     )
    # ]


    @admin.display(description="Rasmi")
    def get_image(self, book):
        if book.image:
            return mark_safe(f'<img src="{book.image.url}" width="150px">')
        return '-'

    # get_image.short_description = "Rasmi"

    @admin.display(description="Muqaddima")
    def get_introduction(self, book):
        if len(book.introduction) > 50:
            return book.introduction[:50] + "..."
        return book.introduction

    @admin.display(boolean=True, description="Tekiruvdan o'tgan")
    def my_test(self, book):
        if book.price > 100:
            return True
        return False

    # get_introduction.short_description = "Muqaddima"


# admin.site.register(Book, BookAdmin)