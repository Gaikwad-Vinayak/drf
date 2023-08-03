from django.urls import path
from core import consumers

websocet_urlpattern=[
    path('ws/<str:groupkname>/',consumers.mycon.as_asgi()),
    # path('wa/',consumers.myacon.as_asgi())
]