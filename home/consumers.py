from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer

from .models import Chat,ChatGroup
from channels.db import database_sync_to_async
import json

from asgiref.sync import async_to_sync

from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

from .models import ChatGroup, Chat

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connected...")
        return super().connect()
    
    def receive(self, text_data=None, bytes_data=None):
        print("Data recieved from client...", text_data)
        self.send(text_data="Message to client from Server...")
        return super().receive(text_data, bytes_data)
    
    def disconnect(self, code):
        print("Websocket disconnected...with code", code)
        return super().disconnect(code)
    

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected...")
        return await super().connect()
    
    async def receive(self, text_data=None, bytes_data=None):
        print("Data recieved from client...", text_data)
        await self.send(text_data="Message to client from Server...")
        return await super().receive(text_data, bytes_data)
    
    async def disconnect(self, code):
        print("Websocket disconnected...with code", code)
        return await super().disconnect(code)