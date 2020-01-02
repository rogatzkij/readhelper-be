from rest_framework import serializers

from bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """Сериализация закладок книги"""

    class Meta:
        model = Bookmark
        fields = ("id", "book", "position", "date")
