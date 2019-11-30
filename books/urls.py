from django.urls import path

from books.views import *

urlpatterns = [
     path('', BookView.as_view()),
     path('page/', PageView.as_view())
]
