from channels.generic.websocket import AsyncWebsocketConsumer
import json
import datetime

class QRConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("📡 Nouveau client connecté")

    async def receive(self, text_data=None, bytes_data=None):
        try:
            data = json.loads(text_data)
            pseudo = data.get("pseudo", "user123")
            qr_code = data.get("qr_code", "")

            if qr_code:
                # Log console
                print(f"[{datetime.datetime.now()}] {pseudo} → {qr_code}")

                # Exemple stockage dans un fichier
                with open("qr_logs.txt", "a") as f:
                    f.write(f"{datetime.datetime.now()} | {pseudo} | {qr_code}\n")

                # Réponse client
                await self.send(json.dumps({"status": "ok", "msg": f"QR reçu de {pseudo}"}))
        except Exception as e:
            await self.send(json.dumps({"error": str(e)}))
