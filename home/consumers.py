from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
from asgiref.sync import async_to_sync
from .models import ChatGroup, Chat
import json

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("Websocket connected...")
        self.accept()        
    
    def receive_json(self, content,**kwargs):
      print("Data recieved from client...",content)
      self.send_json({'msg':'Message from server to client...'})
        

    def disconnect(self, close_code):
         print("Websocket disconnected...with code", close_code)











# get group name from url parameter
        # self.group_name = self.scope['url_route']['kwargs']['group_name']
        # # add channel to group
        # async_to_sync(self.channel_layer.group_add)(
        #     self.group_name,
        #     self.channel_name  # Use channel_name here, not channel_layer
        # )
          # Accept the WebSocket connection

# message = json.loads(text_data)['msg']
        # group = ChatGroup.objects.get(name=self.group_name)

        # if self.scope['user'].is_authenticated:
            
        #     chat= Chat(content=message,group=group)
        #     chat.save()
        #     # send the message to the group
        #     async_to_sync(self.channel_layer.group_send)(
        #         self.group_name,
        #         {
        #             'type': 'chat.message',
        #             'message': message
        #         }
        #     )
        # else:
        #     self.send(text_data=json.dumps({
        #         "message": "Login Required"
        #     }))

    # def chat_message(self, event):
    #     # Send the message to the WebSocket client
    #     self.send(text_data=json.dumps({
    #         'message': event['message']
    #     }))













        # Remove channel from group
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.group_name,
        #     self.channel_name
        # )
        

    

# class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print("Websocket Connected...")
#         return await super().connect()
    
#     async def receive(self, text_data=None, bytes_data=None):
#         print("Data recieved from client...", text_data)
#         await self.send(text_data="Message to client from Server...")
#         return await super().receive(text_data, bytes_data)
    
#     async def disconnect(self, code):
#         print("Websocket disconnected...with code", code)
#         return await super().disconnect(code)