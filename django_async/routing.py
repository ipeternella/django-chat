"""
Module with routing configuration used by Channels. Used to route requests
with DIFFERENT protocols to be handled by different CONSUMERS (ASGI applications).

ProtocolTypeRouter itself is the main ASGI application that wraps many consumers. This
application is served to Daphne ASGI app server.
"""
from channels.routing import ProtocolTypeRouter

# main ASGI application for ASGI application servers
application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
    }
)
