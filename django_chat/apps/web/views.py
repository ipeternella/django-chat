"""
Views for the web app.
"""
import logging

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request: HttpRequest, chat_room: str, chat_user: str) -> HttpResponse:
    """
    Index page of the web app.
    """
    logger.info("New user: %s has joined the chat room: %s", chat_room, chat_user)

    return render(request, template_name="web/index.html", context={"user_name": "igp!"})
