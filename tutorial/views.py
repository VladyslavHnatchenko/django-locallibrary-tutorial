from django.shortcuts import render
from django_tables2 import RequestConfig

from catalog.models import Book
from .models import Person
from .tables import PersonTable, BookTable


def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "tutorial/people.html", {"table": table})


def books(request):
    table = BookTable(Book.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "tutorial/books.html", {"table": table})
