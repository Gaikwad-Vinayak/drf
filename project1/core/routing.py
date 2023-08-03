
from .import consumers
from django.urls import path

websocket_urlpatterns=[
    path('ws/',consumers.syncconsumer.as_asgi()),
    path('wa/',consumers.asycconsumer.as_asgi()),
]
