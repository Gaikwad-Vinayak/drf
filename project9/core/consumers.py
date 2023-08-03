from time import sleep
from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

class mysycn(JsonWebsocketConsumer):
    
    def connect(self):
        print('websocket connect........')
        self.group_name=self.scope['url_route']['kwargs']['groupkname']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        
        self.accept()
    
    def receive_json(self, content, **kwargs):
        print('message received............',content)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message':content['msg'],
            }
        )

    def chat_message(self,event):
        self.send_json({
            'message':event['message']
        })
    def disconnect(self, code):
            print('websocket disconnect..........') 