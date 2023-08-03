from time import sleep
from channels.generic.websocket import JsonWebsocketConsumer
from .models import chat
class mysycn(JsonWebsocketConsumer):
    
    def connect(self):
        print('websocket connect........')
        self.accept()
    
    def receive_json(self, content, **kwargs):
        print('message received............',content)
        for i in range(10):
            self.send_json({'message':str(i)})
            sleep(1)
        a=chat(content.data['i'])
        a.save()

    def disconnect(self, code):
            print('websocket disconnect..........')