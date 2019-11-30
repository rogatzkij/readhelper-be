from django.db import models
# Create your models here.
from django.contrib.auth.models import User
import random
import json

class Book(models.Model):
    '''Книжка'''
    owner = models.ForeignKey(User, verbose_name="Владелец книги", on_delete=models.CASCADE)

    filename = models.CharField(verbose_name="Название файла", max_length=50)
    date = models.DateField(verbose_name="Дата создания")
    current = models.IntegerField(verbose_name="Текущая страница")
    count = models.IntegerField(verbose_name="Всего страниц")

    # bookmarks
    # hash
    # color

    def get_page(self, page):
        words = []
        en = ("cat", "dog")
        ru = ("кот", "пес")
        postfix = ("", "!", ",")
        status= ("NEW", "LEARNING", "KNOWN")

        for i in range(50):
            words.append(Book.Word(i+page*50, random.choice(en), random.choice(ru), postfix=random.choice(postfix), status=random.choice(status)))
        return words

    class Word:
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
        def __json__(self):
            return json.dumps(self.__dict__)
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"