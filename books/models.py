import os
import random

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Модели readhelper
from readhelper.settings import LOCAL_BOOK_STORAGE
from dictionary.models import TranslateWord

# Библиотеки для работы с текстом
import string
from textblob import Word as LemmatizeWord

class Book(models.Model):
    """Класс описывает Книгу"""
    #  Информация о книге
    owner = models.ForeignKey(User, verbose_name="Владелец книги", on_delete=models.CASCADE)
    filename = models.CharField(verbose_name="Название файла", max_length=50)
    local_file = models.CharField(verbose_name="Файл на сервере", max_length=50)
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
        # Все слова на странице
        words = []

        # Все слова в книге
        all_words = []

        # Тестовые данные
        status = ("NEW", "LEARNING", "KNOWN")

        # Читаем все слова из книги
        with open(os.path.join(LOCAL_BOOK_STORAGE, self.local_file)) as file_book:
            for line in file_book:
                all_words.extend(line.split(' '))

        # Формируем список слов на текущей странице
        for i in range(page * self.page_size, page * self.page_size + self.page_size):
            # Отсекаем знаки препинания
            word_without_postfix = all_words[i].rstrip(string.whitespace).rstrip(string.punctuation)
            postfix = all_words[i][len(word_without_postfix):]

            try:
                # Лематизируем слово
                word = word_without_postfix.lower()
                word = LemmatizeWord(word).lemmatize()

                # Находим слово в базе
                word = TranslateWord.objects.get(word=word)

                # Добавляем в список переводов слов на странице
                words.append(Book.Word(i,
                                       word_without_postfix,
                                       word.translate,
                                       dict_id=word.word_id,
                                       postfix=postfix,
                                       level=word.frequency,
                                       status=random.choice(status)))
            except:
                # Если не нашли
                words.append(Book.Word(
                    i,
                    word_without_postfix,
                    "Перевод не найден",
                    postfix=postfix,
                    status=random.choice(status)))

        # Сохраняем текущую страницу
        self.current = page
        # Сохраняем кол-во страниц
        self.count = int(len(all_words) / self.page_size) - 1
        self.save()

        return words

    class Word:
        """Класс описывает переведенное слово"""

        def __init__(self, position, word, translate, dict_id='-1', level='-1', status='NEW', postfix=''):
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
