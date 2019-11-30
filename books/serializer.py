#  Для сериализации
from django.contrib.auth.models import User
from rest_framework import serializers

from books.models import Book


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class BookSerializer(serializers.ModelSerializer):
    """Сериализация книги"""

    class Meta:
        model = Book
        fields = ("id", "filename", "date", "current", "count", "page_size")


class WordSerializer(serializers.Serializer):
    dict_id = serializers.IntegerField()
    position = serializers.IntegerField()
    word = serializers.CharField(max_length=20)
    level = serializers.IntegerField()
    status = serializers.CharField(max_length=10)
    translate = serializers.CharField(max_length=20)
    postfix = serializers.CharField(max_length=10)
