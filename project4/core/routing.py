from django.urls import path
from core import consumers

websocket_urlpattern=[
    path('ws/',consumers.EchoConsumer.as_asgi())

]