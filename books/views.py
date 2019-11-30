from django.shortcuts import render
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse
import json
from rest_framework.renderers import JSONRenderer

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
            book_id = int( request.GET.get("book"))
            page = int(request.GET.get("page"))
        except:
            return Response(status=400)

        try:
            book = Book.objects.get(id=book_id)
            words = book.get_page(page)
        except:
            return Response(status=404)

        serializer = WordSerializer(words, many=True)
        return JsonResponse({'words':serializer.data})