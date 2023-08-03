from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync

class synccon(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })
        async_to_sync(self.channel_layer.group_add)(
            "chat", 
            self.channel_name
            )

    def websocket_receive(self, event):
        print('message send')
        self.send({
            "type": "websocket.send",
            # "text": event["text"],
            "text": 'send server',
        })

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)
        (
            "chat", 
            self.channel_name
        )