import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from User.models import User
from .models import Messages

class ChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username_from = int(self.scope['url_route']['kwargs']['username_from'])
        self.username_to = int(self.scope['url_route']['kwargs']['username_to'])
        self.room_channel_name = f"chat_{min(self.username_from, self.username_to)}_{max(self.username_from, self.username_to)}"

        # accept connection
        await self.channel_layer.group_add(
            self.room_channel_name,
            self.channel_name
        )

        await self.accept()
        # await self.accept()

    async def disconnect(self, close_code):
        pass

        # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json["from"]
        receiver = text_data_json["to"]
    
        await self.channel_layer.group_send(
            self.room_channel_name,{
                "type" : "message",
                "message" : message , 
                "from" : sender , 
                "to" : receiver,
            })
        await self.save_message_to_database(sender, receiver,message)
        print(message, sender, receiver)
        # print("Message saved:", message, "from:", sender, "to:", receiver)

    async def message(self, event):
        await self.send(text_data=json.dumps({
        'message': event['message'],
        'username_from': event['from'],
        'username_to': event['to'],
        'timestamp': 'event',
    }))
        
    @database_sync_to_async
    def save_message_to_database(self, sender, receiver, content):
        print('aaye ma')
        print(sender, receiver, content)
        sender_user = User.objects.get(id = sender)
        receiver_user = User.objects.get(id = receiver)
        print(sender_user)
        print(receiver_user)

        # Save the message to the database
        messagee = Messages.objects.create(
            sender=sender_user,
            receiver=receiver_user,
            message=content,
        )
        print("messagee")
        return messagee
            
