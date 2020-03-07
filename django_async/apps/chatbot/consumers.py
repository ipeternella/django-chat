"""
Module with consumers for the chatbot app.
"""
import json
import logging

from channels.generic.websocket import WebsocketConsumer
from django_async.apps.chatbot.support.utils import get_chat_room_from_url
from django_async.apps.chatbot.support.utils import get_chat_user_from_url

logger = logging.getLogger(__name__)


class ChatConsumer(WebsocketConsumer):
    """
    Websocket chat consumer.
    """

    def connect(self):
        logger.info("Received new socket connection...")

        self.accept()

    def disconnect(self, close_code):
        logger.info("Received socket disconnection...")
        pass

    def receive(self, text_data):
        chat_room = get_chat_room_from_url(self.scope)
        chat_user = get_chat_user_from_url(self.scope)

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        logger.info("New message: %s at chat room: %s from user: %s", message, chat_room, chat_user)

        self.send(text_data=json.dumps({"message": message}))
