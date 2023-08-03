from email import message
import json
from re import A
from time import sleep
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class mycon(WebsocketConsumer):

    def connect(self):
        print('connection connect')
        self.group_name=self.scope['url_route']['kwargs']['groupkname']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        print('data receive')
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message':message
            }
        )
        

    def disconnect(self, code):
        print('disconnect')


    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'msg':event['message']
        }))

# class myacon(AsyncWebsocketConsumer):
    
#     async def connect(self):
#             print('connection connect')
#             await self.accept()
    
#     async def receive(self, text_data=None, bytes_data=None):
#             print('data receive')
#             for i in range(10):
#                 await self.send(text_data='hello')
                
    
#     async def disconnect(self, code):
#             print('disconnect')