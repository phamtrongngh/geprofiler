from django.contrib import admin
from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r"^pets$", views.pets),
    url(r"^owners$", views.owners),
]
