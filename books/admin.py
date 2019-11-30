from django.contrib import admin

# Register your models here.
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    ''''Книги'''

    list_display = ("owner", "filename", "current", "count", "page_size")

admin.site.register(Book, BookAdmin)