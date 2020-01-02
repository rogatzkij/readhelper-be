from django.contrib import admin

from bookmarks.models import Bookmark


# Register your models here.


class BookmarkAdmin(admin.ModelAdmin):
    """Закладки"""

    list_display = ("id", "book", "position", "date")


admin.site.register(Bookmark, BookmarkAdmin)
