from django.contrib import admin

# Register your models here.
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    ''''Книги'''

    list_display = ("id", "owner", "filename", "local_file", "current", "count")

admin.site.register(Book, BookAdmin)