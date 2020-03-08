import uuid

from django.db import models


class StandardModelMixin(models.Model):
    """
    Abstract class for models.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True


class ChatUser(StandardModelMixin):
    """
    Models a simple chat message.
    """

    name = models.CharField(max_length=255, unique=True)


class ChatRoom(StandardModelMixin):
    """
    Models a simple chat room.
    """

    name = models.CharField(max_length=255, unique=True)


class ChatMessage(StandardModelMixin):
    """
    Models a simple chat message.
    """

    message = models.CharField(max_length=255)
    user = models.ForeignKey(to=ChatUser, related_name="chat_user", on_delete=models.CASCADE)
    room = models.ForeignKey(to=ChatRoom, related_name="chat_room", on_delete=models.CASCADE)
