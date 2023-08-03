from django.urls import path
from core import consumers
websocket_urlpattern=[
    path('ws/',consumers.myconsumer.as_asgi())
]