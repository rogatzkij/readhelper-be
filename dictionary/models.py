from django.db import models

# Create your models here.

class TranslateWord(models.Model):
    word = models.CharField(verbose_name="Слово", primary_key=True, max_length=15)
    translate = models.CharField(verbose_name="Перевод", max_length=15)
    frequency = models.IntegerField(verbose_name="Частота")

    class Meta:
        verbose_name = "Переведенное слово"
        verbose_name_plural = "Переведенные слова"