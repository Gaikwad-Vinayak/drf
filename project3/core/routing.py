from django.urls import path
from .import consumers

websocket_urlpatterns=[
    path('ws/',consumers.synccon.as_asgi())
]