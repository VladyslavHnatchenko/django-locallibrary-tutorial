import django_tables2 as tables

from catalog.models import Book, Genre, Language, Author
from .models import Person


class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"


class BookTable(tables.Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"


class GenreTable(tables.Table):
    class Meta:
        model = Genre
        template_name = "django_tables2/bootstrap.html"


class LanguageTable(tables.Table):
    class Meta:
        model = Language
        template_name = "django_tables2/bootstrap.html"


class AuthorTable(tables.Table):
    class Meta:
        model = Author
        template_name = "django_tables2/bootstrap.html"
