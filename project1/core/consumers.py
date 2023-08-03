from channels.consumer import SyncConsumer,AsyncConsumer
import asyncio
from time import sleep

class syncconsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        for i in range(20):
             self.send({
                "type": "websocket.send",
                "text": str(i)
            })
             sleep(1)
    
    def websocket_disconect(self, event):
        print('disconnected websokect')
    

class asycconsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        for i in range(20):
            await self.send({
                "type": "websocket.send",
                "text": str(i)
            })
            await asyncio.sleep(1)
    async def websocket_disconect(self, event):
        print('disconnected websokect')
 