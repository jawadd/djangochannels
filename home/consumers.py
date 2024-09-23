from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        # get default channel layer from the project
        print("Channel Layer:...",self.channel_layer)

         # get default channel name from the project
        print("Channel Name:...",self.channel_name)

        # Add  channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(
             'Programmers', #group name
         self.channel_name
         )

       # print("Websocket connected...")

        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print("Message recieved from client is ",event)
        async_to_sync(self.channel_layer.group_send)(
             'Programmers',
         {
            'type':'chat.message',
            'message': event['text']
        }
        )
        # event handler for chat.message, i.e chat.message is an event
    def chat_message(self,event):
            print("Event...",event['message'])
            self.send({
                 'type':'websocket.send',
                 'text': event['message']
            })

    def websocket_disconnect(self,event):

        print("Channel Layer:...",self.channel_layer)

         # get default channel name from the project
        print("Channel Name:...",self.channel_name)

        async_to_sync(self.channel_layer.group_discard)
        ('Programmers', #group name
         self.channel_name
         )

        raise StopConsumer()

class MyASyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        # get default channel layer from the project
        print("Channel Layer:...",self.channel_layer)

         # get default channel name from the project
        print("Channel Name:...",self.channel_name)

        # Add  channel to a new or existing group
        await self.channel_layer.group_add(
             'Programmers', #group name
         self.channel_name
         )

       # print("Websocket connected...")

        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print("Message recieved from client is ",event)
        await self.channel_layer.group_send(
             'Programmers',
         {
            'type':'chat.message',
            'message': event['text']
        }
        )
        # event handler for chat.message, i.e chat.message is an event
    async def chat_message(self,event):
            print("Event...",event['message'])
            await self.send({
                 'type':'websocket.send',
                 'text': event['message']
            })

    async def websocket_disconnect(self,event):

        print("Channel Layer:...",self.channel_layer)

         # get default channel name from the project
        print("Channel Name:...",self.channel_name)

        await self.channel_layer.group_discard
        ('Programmers', #group name
         self.channel_name
         )

        raise StopConsumer()
















# from channels.generic.websocket import WebsocketConsumer
# from channels.consumer import SyncConsumer,AsyncConsumer
# from channels.exceptions import StopConsumer
# from time import sleep
# import asyncio
# import json


# class MySyncConsumer(SyncConsumer):

#     def websocket_connect(self,event):
#         print("Websocket connected...")
#         self.send({
#             'type':'websocket.accept'
#         })

#     # def websocket_receive(self,event):
#     #     print("Message recieved from client is ",event['text'])
#     #     for i in range(7):
#     #         self.send({
#     #             'type':'websocket.send',
#     #             'text':str(i)
#     #         })
#     #         sleep(1)
#     def websocket_receive(self,event):
#         print("Message recieved from client is ",event['text'])
#         for i in range(7):
#             self.send({
#                 'type':'websocket.send',
#                 'text':json.dumps({"count":i})
#             })
#             sleep(1)


#     def websocket_disconnect(self,event):
#         print("Websocket disconnected...")
#         raise StopConsumer()

# class MyAsyncConsumer(AsyncConsumer):

#     async def websocket_connect(self,event):
#         print("Websocket connected...")
#         await self.send({
#             'type':'websocket.accept'
#         })

#     async def websocket_receive(self,event):
#         print("Message recieved from client is ",event['text'])
#         for i in range(30):
#            await self.send({
#                 'type':'websocket.send',
#                 'text':str(i)
#             })
#            await asyncio.sleep(1)
            
       

#     async def websocket_disconnect(self,event):
#         print("Websocket disconnected...")
#         raise StopConsumer()