"""
Command functions used by the chat bot.
"""
import asyncio

from django.utils.timezone import now
from django_chat.apps.chat.support.utils import get_chat_room_from_url
from django_chat.settings import BOT_USER_NAME


async def command_now(chat_consumer, *args, **kwargs) -> None:
    message = f"The time right now is {now()}"
    bot_user_name = BOT_USER_NAME
    chat_room = get_chat_room_from_url(chat_consumer.scope)

    await chat_consumer.send_to_channels_group(message, bot_user_name, channel_group=chat_room)


async def send_sms(chat_consumer, *args, **kwargs) -> None:
    user_to_receive_sms = args[0]
    chat_room = get_chat_room_from_url(chat_consumer.scope)

    message = f"An SMS has been sent to {user_to_receive_sms}"
    bot_user_name = BOT_USER_NAME

    await chat_consumer.channel_layer.send(
        "sms_channel", {"type": "send_sms", "message": "hi", "user_name": user_to_receive_sms}
    )
    await asyncio.sleep(2)
    await chat_consumer.send_to_channels_group(message, bot_user_name, channel_group=chat_room)
