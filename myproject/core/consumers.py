from time import sleep
from channels.consumer import SyncConsumer,AsyncConsumer


class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('websocket_connected..')
        await self.send({'type':'websocket.accept'})

    async def websocket_receive(self, event):
        print('websocket_received...',event['text'])
        for i in range(20):
            await self.send({
            "type":"websocket.send",
            "text": str(i)
            })
            await sleep(1)
        
    async def websocket_desconnet(self, event):
        print('websocket_desconnet...')
        