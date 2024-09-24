from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from .models import Chat,ChatGroup
from channels.db import database_sync_to_async
import json

from asgiref.sync import async_to_sync

from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
import json
from .models import ChatGroup, Chat

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        
        # Add the channel to a group (synchronously)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,  # group name
            self.channel_name
        )
        
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message received from client is", event)
        
        # Parse the message data
        data = json.loads(event['text'])

        # Retrieve or create the ChatGroup instance
        group = ChatGroup.objects.get(name=self.group_name)
        
        # Save the chat message to the database
        chat = Chat(content=data['msg'], group=group)
        chat.save()

        # Send the message to the group (synchronously)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat.message',
                'message': event['text']
            }
        )

    def chat_message(self, event):
        print("Event...", event['message'])
        
        # Send the message back to the client
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print("Channel Layer:...", self.channel_layer)
        print("Channel Name:...", self.channel_name)
        
        # Remove the channel from the group (synchronously)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,  # group name
            self.channel_name
        )

        raise StopConsumer()


class MyASyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        # Add  channel to a new or existing group
        await self.channel_layer.group_add(
             self.group_name, #group name
         self.channel_name
         )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print("Message recieved from client is ",event)
        data= json.loads(event['text'])

        
        group = await database_sync_to_async(ChatGroup.objects.get)(name=self.group_name)

        chat=Chat(content=data['msg'],group=group)
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
             self.group_name,
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

        await self.channel_layer.group_discard(
             self.group_name, #group name
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