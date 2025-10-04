from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QRcode
import datetime, os

@receiver(post_save, sender=QRcode)
def log_qrcode(sender, instance, created, **kwargs):
    if created:  # seulement à la création
        print(f"📝 Nouveau QR code créé par {instance.creator} avec IP {instance.ip_address or 'N/A'}")
        with open("qr_logs.txt", "a+", encoding="utf-8") as f:
            f.write(
                f"[{datetime.datetime.now()}] "
                f"Créateur: {instance.creator} | "
                f"IP: {instance.ip_address or 'N/A'} | "
                f"Données: {instance.data}\n"
            )
