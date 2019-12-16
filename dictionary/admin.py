from django.contrib import admin

# Register your models here.
from dictionary.models import TranslateWord

class TranslateWordAdmin(admin.ModelAdmin):
    ''''Переведенные слова'''

    list_display = ("word_id","word", "translate", "frequency")

admin.site.register(TranslateWord, TranslateWordAdmin)