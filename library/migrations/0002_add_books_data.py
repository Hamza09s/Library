from django.db import migrations


def insert_initial_data(apps, schema_editor):
    Author = apps.get_model("library", "Author")
    Book = apps.get_model("library", "Book")

    # Create authors
    author1 = Author.objects.create(first_name="Alexander", last_name="One")
    author2 = Author.objects.create(first_name="Bert", last_name="Two")
    author3 = Author.objects.create(first_name="Charlie", last_name="Three")

    # Create books
    Book.objects.create(title="Harry Potter", author=author1, description="Hello there")
    Book.objects.create(
        title="Django programmming", author=author2, description="hello world"
    )
    Book.objects.create(
        title="Around the world in 80 days", author=author3, description="Travel guide"
    )
    Book.objects.create(
        title="Two days ago", author=author3, description="what happened two days ago"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
