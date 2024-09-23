from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Websocket connected...")
        self.send({
            'type':'websocket.accept'
        })

    # def websocket_receive(self,event):
    #     print("Message recieved from client is ",event['text'])
    #     for i in range(7):
    #         self.send({
    #             'type':'websocket.send',
    #             'text':str(i)
    #         })
    #         sleep(1)
    def websocket_receive(self,event):
        print("Message recieved from client is ",event['text'])
        for i in range(7):
            self.send({
                'type':'websocket.send',
                'text':json.dumps({"count":i})
            })
            sleep(1)


    def websocket_disconnect(self,event):
        print("Websocket disconnected...")
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Websocket connected...")
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print("Message recieved from client is ",event['text'])
        for i in range(30):
           await self.send({
                'type':'websocket.send',
                'text':str(i)
            })
           await asyncio.sleep(1)
            
       

    async def websocket_disconnect(self,event):
        print("Websocket disconnected...")
        raise StopConsumer()