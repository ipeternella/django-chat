from django.contrib import admin
from django_chat.apps.web.models import ChatMessage
from django_chat.apps.web.models import ChatRoom
from django_chat.apps.web.models import ChatUser


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """
    Admin for the chat messages.
    """

    list_display = ("chat_room", "chat_user", "message")

    def chat_user(self, instance: ChatMessage):
        return instance.user.name

    def chat_room(self, instance: ChatMessage):
        return instance.room.name


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    """
    Admin for the chat rooms.
    """

    list_display = ("name",)


@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    """
    Admin for the chat users.
    """

    list_display = ("name",)
