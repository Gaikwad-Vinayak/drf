from channels.consumer import AsyncConsumer,SyncConsumer
from time import sleep
import json
class myconsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        for i in range(20):
             self.send({
                "type": "websocket.send",
                "text": json.dumps({'name':i})
            })
             sleep(1)
    
    def websocket_disconect(self, event):
        print('disconnected websokect')
   