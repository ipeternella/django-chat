"""
Main ASGI application entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting (protocol router).
"""
import os

import django
from channels.routing import get_default_application  # protocol router ASGI app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_async.settings")

django.setup()
application = get_default_application()
