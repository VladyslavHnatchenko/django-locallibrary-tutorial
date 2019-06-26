from django.conf.urls import url
from django.contrib import admin

from tutorial.views import people, books, multiple_tables

urlpatterns = [
    url(r'^people/', people),
    url(r'^books/', books),
    url(r'^multiple_tables/', multiple_tables),
]