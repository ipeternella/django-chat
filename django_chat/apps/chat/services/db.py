"""
Module with functions that reach the database.
"""
import logging

from channels.db import database_sync_to_async
from django.db import transaction
from django_chat.apps.web.models import ChatMessage
from django_chat.apps.web.models import ChatRoom
from django_chat.apps.web.models import ChatUser

logger = logging.getLogger(__name__)


@database_sync_to_async
@transaction.atomic
def persist_chat_message(message: str, chat_room: str, user_name: str):
    logger.info("Getting/creating chat_room and chat_user...")
    chat_room, _ = ChatRoom.objects.get_or_create(name=chat_room)
    chat_user, _ = ChatUser.objects.get_or_create(name=user_name)

    logger.info("Persisting message...")
    chat_message = ChatMessage.objects.create(message=message, user=chat_user, room=chat_room)
