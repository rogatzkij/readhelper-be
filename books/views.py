from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializer import BookSerializer
from books.serializer import WordSerializer


class BookView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse({'books': serializer.data})


class PageView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        try:
            book_id = int(request.GET.get("book"))
            position = int(request.GET.get("position"))
            count = int(request.GET.get("count"))
        except:
            return Response(status=400, data='Не правильный тип параметра book или page')

        try:
            book = Book.objects.get(id=book_id)
            words = book.get_page(position, count)
        except:
            return Response(status=404)

        serializer = WordSerializer(words, many=True)
        return JsonResponse({'words': serializer.data})
