"""
Command functions used by the chat bot.
"""
from typing import List

from django.utils.timezone import now
from django_async.apps.chatbot.support.utils import get_chat_room_from_url


async def command_now(chat_consumer, *args, **kwargs) -> None:
    message = f"The time right now is {now()}"
    user_name = "🤖 CHAT BOT 🤖"
    chat_room = get_chat_room_from_url(chat_consumer.scope)

    await chat_consumer.send_to_channels_group(message, user_name, channel_group=chat_room)
