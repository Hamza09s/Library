from django.http import JsonResponse
from django.views import View
from django.views.generic import (
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Book
from django.urls import reverse_lazy
from django.db.models import Q
from .tasks import send_email


class BookListView(ListView, LoginRequiredMixin):
    model = Book
    template_name = "home.html"
    context_object_name = "books"

    def get_queryset(self):

        queryset = super().get_queryset()  # type: ignore
        author_name = self.request.GET.get("author_name")

        if author_name:
            author_name = author_name.split()[0]
            queryset = queryset.filter(
                Q(author__first_name__icontains=author_name)
                | Q(author__last_name__icontains=author_name)
            )
        return queryset


class BookLikeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        book_id = self.kwargs["book_id"]
        book = get_object_or_404(Book, id=book_id)
        user = request.user

        if user in book.like.all():
            book.like.remove(user)
            liked = False
        else:
            book.like.add(user)
            liked = True

        response = {"liked": liked, "count": book.like.count()}
        return JsonResponse(response)
