"""
ASGI config for project3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

from distutils import core
import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter,ProtocolTypeRouter
import core.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project3.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    'websocket':URLRouter(
        core.routing.websocket_urlpatterns
    )
})

