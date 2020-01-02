from django.db import IntegrityError
from django.http import JsonResponse
from django.utils.timezone import now
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmarks.models import Bookmark
from bookmarks.serializer import BookmarkSerializer
from books.models import Book


# Create your views here.
class BookmarksView(APIView):
    """ Просмотр и добавление закладок """
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        """" Получить список закладок """
        # Достаем параметры из запроса
        try:
            book_id = int(request.GET.get("book"))
        except:
            return Response(status=400, data='Не правильный тип параметра book')

        # Находим нужную книгу
        try:
            book = Book.objects.get(id=book_id)
        except:
            return Response(status=404, data='Книга с таким id не найдена')

        # Получаем закладки в этой книге
        bookmarks = Bookmark.objects.filter(book=book)

        # Сериализуем и выдаем результат в ответе
        serializer = BookmarkSerializer(bookmarks, many=True)
        return JsonResponse({'bookmarks': serializer.data})

    def post(self, request):
        """" Добавить закладку """
        # Достаем параметры из запроса
        try:
            book_id = int(request.GET.get("book"))
            position = int(request.GET.get("position"))
        except:
            return Response(status=400, data='Не правильный тип параметра book или position')

        # Находим нужную книгу
        try:
            book = Book.objects.get(id=book_id)
        except:
            return Response(status=404, data='Книга с таким id не найдена')

        # Добавляем закладку
        try:
            b = Bookmark(book=book, position=position, date=now())
            b.save()
        except IntegrityError:
            return Response(status=409, data='Такая закладка уже существует')

        # Получаем закладки в этой книге
        bookmarks = Bookmark.objects.filter(book=book)

        # Сериализуем и выдаем результат в ответе
        serializer = BookmarkSerializer(bookmarks, many=True)
        return JsonResponse({'bookmarks': serializer.data})

    def delete(self, request):
        # Достаем параметры из запроса
        try:
            bookmark_id = int(request.GET.get("bookmark"))
        except:
            return Response(status=400, data='Не правильный тип параметра bookmark')

        try:
            bookmark = Bookmark.objects.get(id=bookmark_id)
        except:
            return Response(status=404, data='Закладка с таким id не найдена')

        # Запоминаем книгу
        book = bookmark.book

        # Удаляем закладку
        bookmark.delete()

        # Получаем закладки в этой книге
        bookmarks = Bookmark.objects.filter(book=book)

        # Сериализуем и выдаем результат в ответе
        serializer = BookmarkSerializer(bookmarks, many=True)
        return JsonResponse({'bookmarks': serializer.data})
