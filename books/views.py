from django.http import JsonResponse
import json
import uuid
import os
import base64

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book

from books.serializer import BookSerializer
from books.serializer import WordSerializer

from django.utils.timezone import now
from readhelper.settings import LOCAL_BOOK_STORAGE

class BookView(APIView):
    """ Список доступных книг """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        """Получение списка существующих книг"""
        # Получаем существующие книги
        books = Book.objects.filter(owner=request.user)

        # Сериализуем и выдаем результат в ответе
        serializer = BookSerializer(books, many=True)
        return JsonResponse({'books': serializer.data})

    def post(self, request):
        """Загрузка"""
        # Парсим тело запроса
        body_unicode = request.body.decode('utf-8')
        try:
            body = json.loads(body_unicode)
        except Exception as e:
            return Response(status=400, data='Неправильный JSON, ошибка {}'.format(e))

        book = Book()
        try:
            book.filename = body['name']
            data = base64.b64decode(body['data'])
        except KeyError as e:
            return Response(status=400, data='Нет поля {}, используются поля name, data'.format(e))
        except Exception as e:
            return Response(status=400, data='Неизвестная ошибка {}'.format(e))

        # Владелец книги
        book.owner = request.user
        # Дата создания
        book.date = now()
        # Текущая позиция
        book.current = 0

        # Генерируем случайное имя для файла
        book.local_file = str(uuid.uuid4()) + ".txt"

        # Сохраняем файл
        with open(os.path.join(LOCAL_BOOK_STORAGE, book.local_file), 'wb') as file:
            file.write(data)

        # Всего слов
        all_words = []
        with open(os.path.join(LOCAL_BOOK_STORAGE, book.local_file)) as file_book:
            for line in file_book:
                all_words.extend(line.split(' '))
        book.count = len(all_words)

        # Сохраняем книгу
        book.save()

        # Получаем существующие книги
        books = Book.objects.filter(owner=request.user)

        # Сериализуем и выдаем результат в ответе
        serializer = BookSerializer(books, many=True)
        return JsonResponse({'books': serializer.data})


    def delete(self, request):
        """Удаление книги"""
        # Достаем параметры из запроса
        try:
            book_id = int(request.GET.get("book"))
        except:
            return Response(status=400, data='Не правильный тип параметра book')

        # Получаем книгу
        try:
            book = Book.objects.get(id=book_id, owner=request.user)
        except:
            return Response(status=404, data='Книга с таким id не найдена')

        # Удаляем текстовый файл из файловой системы
        path = os.path.join(LOCAL_BOOK_STORAGE, book.local_file)
        try:
            os.remove(path)
        except Exception as e:
            print('Ошибка: \"{}\" при удалении файла \"{}\"'.format(e, path))

        # Удаляем книгу из базы данных
        book.delete()

        # Получаем существующие книги
        books = Book.objects.filter(owner=request.user)

        # Сериализуем и выдаем результат в ответе
        serializer = BookSerializer(books, many=True)
        return JsonResponse({'books': serializer.data})


class PageView(APIView):
    """ Просмотр содержимого книги """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        try:
            book_id = int(request.GET.get("book"))
            position = int(request.GET.get("position"))
            count = int(request.GET.get("count"))
        except:
            return Response(status=400, data='Не правильный тип параметра book, position или count')

        try:
            book = Book.objects.get(id=book_id, owner=request.user)
        except:
            return Response(status=404, data='Книга с таким id не найдена')

        try:
            words = book.get_page(position, count)
        except:
            return Response(status=500, data='Неизветсная ошибка при подготовке книги')

        serializer = WordSerializer(words, many=True)
        return JsonResponse({'words': serializer.data})
