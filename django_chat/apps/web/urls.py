"""
Module with urls for the web app.
"""
from django.urls import re_path
from django_chat.apps.web import views

app_name = "web"

urlpatterns = [
    re_path(r"^chat/(?P<chat_room>\w+)/(?P<chat_user>\w+)/$", views.index, name="index"),
]
