from django.db import models

# Create your models here.
from books.models import Book


class Bookmark(models.Model):
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name="Позиция в книге")
    date = models.DateField(verbose_name="Дата добавления")

    class Meta:
        # Составной ключ (книга-позиция)
        unique_together = (('book', 'position'),)

        # Наименования в панеле админестратора
        verbose_name = "Добавленная закладка"
        verbose_name_plural = "Добавленные закладки"
