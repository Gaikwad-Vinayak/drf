"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import core.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

django.setup()


application = get_asgi_application()

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),
    "websocket":URLRouter(
        core.routing.websocket_urlpatterns
    )
})