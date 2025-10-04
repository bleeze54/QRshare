import qrcode
from django.db import models
from datetime import datetime
import uuid

class QRcode(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    timestamp = models.IntegerField()
    validitytime = models.IntegerField()  # Validité en secondes
    endtime = models.IntegerField()
    creator = models.CharField(max_length=50)
    qr = models.ImageField(upload_to='qr_codes/')
    data= models.TextField(blank=False, null=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.creator} - {self.data[:20]}..."
    #init
    
    def __init__(self, *args, data='', time=3, creator="anonyme", **kwargs):
        super().__init__(*args, **kwargs)
        try:
             
            if data:  # si on passe "data" à l'instanciation
                if any(x in data.lower() for x in ["porn", "crypto", "hack"]):
                    raise ValueError("Données interdites dans le QR code.")

                self.data = data
                self.creator = creator
                self.validitytime = time
                self.timestamp = int(datetime.now().timestamp())
                self.endtime = self.timestamp + self.validitytime

                # Génération du QR en mémoire (optionnel)
                self.qr_img = qrcode.make(data)  # pas stocké en base

                print(f"QR code créé avec succès : {self.data}")
        except Exception as e:
            print(f"Erreur lors de la création du QR code : {e}")

    def __eq__(self, other):
        if not isinstance(other, QRcode):
            return False 
        return self.data == other.data and self.creator == other.creator