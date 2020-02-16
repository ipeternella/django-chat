"""
Module with urls for the web app.
"""
from django.urls import path
from django_async.apps.web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
]
