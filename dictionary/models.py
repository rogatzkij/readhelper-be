from django.db import models

# Create your models here.

class TranslateWord(models.Model):
    word_id = models.AutoField(verbose_name="ID", primary_key=True)
    word = models.CharField(verbose_name="Слово", db_index=True, max_length=15)
    translate = models.CharField(verbose_name="Перевод", max_length=15)
    frequency = models.IntegerField(verbose_name="Частота")

    class Meta:
        verbose_name = "Переведенное слово"
        verbose_name_plural = "Переведенные слова"