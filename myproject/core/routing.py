from .import consumers
from django.urls import path

websocket_urlpatterns=[
    path('w/',consumers.EchoConsumer.as_asgi())
    ]