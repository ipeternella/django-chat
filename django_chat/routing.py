"""
Module with routing configuration used by Channels. Used to route requests
with DIFFERENT protocols to be handled by different CONSUMERS (ASGI applications).

ProtocolTypeRouter itself is the main ASGI application that wraps many consumers. This
application is served to Daphne ASGI app server.
"""
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ChannelNameRouter
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django_chat.apps.chat.consumers import SMSChannelConsumer
from django_chat.apps.chat.urls import websocket_urlpatterns

# main ASGI application for ASGI application servers
application = ProtocolTypeRouter(
    {
        "http": AsgiHandler,
        "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlpatterns))),
        "channel": ChannelNameRouter({"sms_channel": SMSChannelConsumer}),
    }
)
