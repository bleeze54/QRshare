from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

class QRConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Récupération de l'adresse IP
        client_ip, _ = self.scope.get("client", ("0.0.0.0", 0))
        self.client_ip = client_ip  

        await self.channel_layer.group_add("qrcodes", self.channel_name)
        await self.accept()
        print(f"📡 Client connecté au groupe qrcodes depuis {self.client_ip}")

    async def receive(self, text_data=None, bytes_data=None):
        from .models import QRcode
        data = json.loads(text_data)
        pseudo = data.get("pseudo", "user123")
        qr_code = data.get("qr_code", "")

        if qr_code:
            # Sauvegarde en base (ip incluse)
            await sync_to_async(QRcode.objects.create)(
                data=qr_code,
                creator=pseudo,
                ip_address=self.client_ip   # 🔑 Ici
            )

            # Broadcast à tous les clients connectés
            await self.channel_layer.group_send(
                "qrcodes",
                {
                    "type": "new_qrcode",
                    "creator": pseudo,
                    "ip": self.client_ip,   # 🔑 On la renvoie aussi
                    "data": qr_code,
                }
            )

    async def new_qrcode(self, event):
        await self.send(json.dumps({
            "creator": event["creator"],
            "ip": event["ip"],
            "data": event["data"],
        }))
