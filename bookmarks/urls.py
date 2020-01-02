from django.urls import path

from bookmarks.views import BookmarksView

urlpatterns = [
    path('', BookmarksView.as_view())
]
