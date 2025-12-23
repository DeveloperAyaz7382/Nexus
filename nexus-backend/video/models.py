from django.db import models

# Create your models here.
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_add(self.room, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room,
            {'type':'signal','message':text_data}
        )

    async def signal(self, event):
        await self.send(text_data=event['message'])
