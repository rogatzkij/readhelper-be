import random

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """Класс описывает Книгу"""
    #  Информация о книге
    owner = models.ForeignKey(User, verbose_name="Владелец книги", on_delete=models.CASCADE)
    filename = models.CharField(verbose_name="Название файла", max_length=50)
    date = models.DateField(verbose_name="Дата создания")

    # Все что касается страниц книги
    current = models.IntegerField(verbose_name="Текущая страница")
    count = models.IntegerField(verbose_name="Всего страниц")
    page_size = models.IntegerField(verbose_name="Размер страницы")

    # bookmarks
    # hash
    # color

    def get_page(self, page):
        """Метод служит для получения странцы (заглушка)"""
        words = []
        en = ("cat", "dog")
        ru = ("кот", "пес")
        postfix = ("", "!", ",")
        status = ("NEW", "LEARNING", "KNOWN")


        for i in range(self.page_size):
            words.append(Book.Word(i + page * self.page_size, random.choice(en), random.choice(ru),
                                   postfix=random.choice(postfix), status=random.choice(status)))

        # Сохраняем текущую страницу
        self.current = page
        self.save()

        return words

    class Word:
        """Класс описывает переведенное слово"""

        def __init__(self, position, word, translate, dict_id='-1', level='0', status='NEW', postfix=''):
            # id  в словаре
            self.dict_id = dict_id
            # позиция в книге
            self.position = position
            # исходное слово
            self.word = word
            #
            self.level = level
            # NEW, LEARNING, KNOWN
            self.status = status
            # перевод
            self.translate = translate
            # знаки препиания
            self.postfix = postfix

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
