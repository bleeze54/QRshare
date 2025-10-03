from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

class QRConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("qrcodes", self.channel_name)
        await self.accept()
        print("📡 Client connecté au groupe qrcodes")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("qrcodes", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        from .models import QRcode
        data = json.loads(text_data)
        pseudo = data.get("pseudo", "user123")
        qr_code = data.get("qr_code", "")

        if qr_code:
            # Sauvegarde en base (en thread séparé)
            await sync_to_async(QRcode.objects.create)(
                data=qr_code, creator=pseudo
            )

            # Broadcast à tous les clients connectés
            await self.channel_layer.group_send(
                "qrcodes",
                {
                    "type": "new_qrcode",
                    "creator": pseudo,
                    "data": qr_code,
                }
            )

    async def new_qrcode(self, event):
        # Envoi JSON au navigateur
        await self.send(json.dumps({
            "creator": event["creator"],
            "data": event["data"],
        }))
