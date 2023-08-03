from time import sleep
from channels.consumer import SyncConsumer


class myconsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket_connected..')
        self.send({'type':'websocket.accept'})

    def websocket_receive(self, event):
        print('websocket_received...',event['text'])
        
        self.send({
            "type":"websocket.send",
            "text": 'message ricived'
        })
           
            
        
    def websocket_desconnet(self, event):
        print('websocket_desconnet...')
        