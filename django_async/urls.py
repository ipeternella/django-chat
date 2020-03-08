"""
Django project url configurations.
"""
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("django_chat.apps.web.urls")),
    path("admin/", admin.site.urls),
]
