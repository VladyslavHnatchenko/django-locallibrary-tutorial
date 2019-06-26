from django.shortcuts import render
from django_tables2 import RequestConfig

from catalog.models import Book, Genre, Language, Author
from .models import Person
from .tables import PersonTable, BookTable, GenreTable, LanguageTable, AuthorTable


def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "tutorial/people.html", {"table": table})


def books(request):
    table = BookTable(Book.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "tutorial/books.html", {"table": table})


def multiple_tables(request):
    books_table = BookTable(Book.objects.all())
    genres_table = GenreTable(Genre.objects.all())
    languages_table = LanguageTable(Language.objects.all())
    authors_table = AuthorTable(Author.objects.all())

    RequestConfig(request, paginate=False).configure(books_table)
    RequestConfig(request, paginate=False).configure(genres_table)
    RequestConfig(request, paginate=False).configure(languages_table)
    RequestConfig(request, paginate=False).configure(authors_table)

    all_tables = {
        "books_table": books_table,
        "genres_table": genres_table,
        "languages_table": languages_table,
        "authors_table": authors_table,
    }

    return render(request, "tutorial/multiple_tables.html", all_tables)
