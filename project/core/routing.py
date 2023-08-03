from django import urls
from .import consumers
from django.urls import path

websocket_urlpatterns=[
    path('w/',consumers.myconsumer.as_asgi())
    ]