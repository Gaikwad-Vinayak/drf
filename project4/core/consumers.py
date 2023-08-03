from tokenize import group
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        async_to_sync(self.channel_layer.group_add)
        'group1',
        self.channel_name
             
        self.send({
            "type": "websocket.accept",
            
        })


    def websocket_receive(self, event):
        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        #     "text": "vinayak",
        # })
        print(event)
        async_to_sync(self.channel_layer.group_send)('group1',{
            'type':'chat.system_message',
            'message':event['text']
            })

    def websocket_disconnect(self,event):
        async_to_sync(self.channel_layer.group_discard)("group1", self.channel_name)


    def chat_message(self, event):
        self.send(event["message"])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
