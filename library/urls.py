from django.urls import path
from .views import BookListView, BookLikeView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("books/<int:book_id>/like/", BookLikeView.as_view(), name="like_book"),
]
