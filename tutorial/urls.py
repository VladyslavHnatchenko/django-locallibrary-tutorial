from django.conf.urls import url
from django.contrib import admin

from tutorial.views import people, books

urlpatterns = [
    url(r'^people/', people),
    url(r'^books/', books),
]