"""
Module with consumers for the chat app.
"""
import asyncio
import json
import logging
from typing import Optional

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from django_chat.apps.bot.business.commands import run_command
from django_chat.apps.bot.business.utils import get_command_from_user_message
from django_chat.apps.chat.services.db import persist_chat_message
from django_chat.apps.chat.support.utils import get_chat_room_from_url
from django_chat.apps.chat.support.utils import get_chat_user_from_url
from django_chat.settings import BOT_USER_NAME

logger = logging.getLogger(__name__)


class SMSChannelConsumer(AsyncConsumer):
    """
    SMS consumer that listens on the fixed name channel 'sms_channel'.
    """

    async def send_sms(self, event):
        logger.info("Sending SMS to %s", event["user_name"])
        await asyncio.sleep(2)
        logger.info("Successfully sent SMS!")


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Websocket chat consumer.
    """

    async def connect(self):
        logger.info("Received new socket connection...")
        chat_room = get_chat_room_from_url(self.scope)
        user_name = get_chat_user_from_url(self.scope)
        current_channel_name = self.channel_name
        bot_user_name = BOT_USER_NAME

        await self.channel_layer.group_add(chat_room, self.channel_name)
        logger.info(
            "Added socket connection channel %s to channel group (chat room): %s", current_channel_name, chat_room
        )

        await self.send_to_channels_group(
            f"A new user, {user_name}, has joined the room! Stay a while and listen!", bot_user_name, chat_room
        )

        await self.accept()

    async def disconnect(self, close_code):
        logger.info("Received socket disconnection...")
        pass

    async def receive(self, text_data):
        chat_room = get_chat_room_from_url(self.scope)
        chat_user = get_chat_user_from_url(self.scope)

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        logger.info("New message: %s at chat room: %s from user: %s", message, chat_room, chat_user)
        await self.send_to_channels_group(message, user_name=chat_user, channel_group=chat_room)

    async def chat_message_to_channel_group(self, event):
        await self.send(text_data=json.dumps(event))

    async def send_to_channels_group(self, message: str, user_name: str, channel_group: Optional[str]):
        chat_room = get_chat_room_from_url(self.scope)
        final_message = f"{user_name}: {message}"

        if channel_group:
            logger.info("Sending msg to a group of channels: %s", channel_group)

            logger.info("Extracting commands from user message...")
            cmd, cmd_args = get_command_from_user_message(message)

            if cmd is not None:
                logger.info("Detected cmd...")
                await run_command(cmd, cmd_args, self)

            else:
                logger.info("No commands detected...")
                await persist_chat_message(final_message, chat_room, user_name)

                await self.channel_layer.group_send(
                    channel_group, {"type": "chat_message_to_channel_group", "message": final_message}
                )

            return

        # no channels layers: sending only to the current websocket channel
        logger.info("Sending msg to a single channel...")
        await self.send(text_data=json.dumps({"message": final_message}))
