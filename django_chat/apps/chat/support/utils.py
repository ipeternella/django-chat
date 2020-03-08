"""
Module with utility functions for the chat app.
"""
from typing import Dict


def get_chat_room_from_url(scope: Dict) -> str:
    """
    Gets the room name from the url.
    """
    return scope["url_route"]["kwargs"]["chat_room"]


def get_chat_user_from_url(scope: Dict) -> str:
    """
    Gets the room name from the url.
    """
    return scope["url_route"]["kwargs"]["chat_user"]
