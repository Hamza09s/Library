from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey("Author", on_delete=models.RESTRICT)
    description = models.TextField(max_length=1000, help_text="Description of book")
    like = models.ManyToManyField(
        get_user_model(), related_name="books_liked", blank=True
    )

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name
