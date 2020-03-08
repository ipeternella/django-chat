"""
Module with routing configuration used by Channels. Used to route requests
with DIFFERENT protocols to be handled by different CONSUMERS (ASGI applications).

ProtocolTypeRouter itself is the main ASGI application that wraps many consumers. This
application is served to Daphne ASGI app server.
"""
from channels.http import AsgiHandler
from channels.routing import ChannelNameRouter
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from django_chat.apps.chatbot.consumers import SMSChannelConsumer
from django_chat.apps.chatbot.urls import websocket_urlpatterns

# main ASGI application for ASGI application servers
application = ProtocolTypeRouter(
    {
        "http": AsgiHandler,
        "websocket": URLRouter(websocket_urlpatterns),
        "channel": ChannelNameRouter({"sms_channel": SMSChannelConsumer}),
    }
)
