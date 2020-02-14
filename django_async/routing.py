"""
Module with routing configuration used by Channels. Used to route requests
with DIFFERENT protocols to be handled by different CONSUMERS (ASGI applications).
"""
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
    }
)
