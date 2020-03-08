"""
Module with the urls for the chatbot app.
"""
from django.urls import re_path
from django_chat.apps.chatbot.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_room>\w+)/(?P<chat_user>\w+)/$", ChatConsumer),
]
