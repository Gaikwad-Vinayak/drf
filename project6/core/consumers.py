from time import sleep
from channels.consumer import AsyncConsumer,SyncConsumer
from asgiref.sync import async_to_sync

class myconsumer(SyncConsumer):

    def websocket_connect(self, event):
             
        self.send({
            "type": "websocket.accept",
            
        })
        async_to_sync(self.channel_layer.group_add)
        'programer',
        self.channel_name


    def websocket_receive(self, event):
        print('hello')
        self.send({
                'type':'websocket.send',
                "text": event["text"],
            })
        async_to_sync(self.channel_layer.group_send('programer',
        {'type':'chat.message','message':event['text']}))
    def websocket_desconnect(self, event):
        async_to_sync(self.channel_layer.group_discard('programer'),self.channel_name)
        print('desconnect')