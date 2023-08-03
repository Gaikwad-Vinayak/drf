from time import sleep
from channels.consumer import AsyncConsumer,SyncConsumer

class myconsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })
    def websocket_receive(self, event):
        print('hello')
        for i in range(5):
            self.send({
                'type':'websocket.send',
                'text':str(i),
                # "text": event["text"],
            })
            sleep(1)
    def websocket_desconnect(self, event):
        print('desconnect')