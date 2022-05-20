from django.contrib import admin
from django.urls import re_path as url

from . import views

urlpatterns = [
    url("admin/", admin.site.urls),
    url(r"^$", views.hello_world),
    url("post/", views.post),
]
