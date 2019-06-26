import django_tables2 as tables

from catalog.models import Book
from .models import Person


class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"


class BookTable(tables.Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
