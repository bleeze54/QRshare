from django.apps import AppConfig
import threading, datetime, time
from django.utils import timezone

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from app.models import QRcode
        import app.signals  # ⬅️ importer les signaux

        # Thread de nettoyage des QR codes expirés
        def cleaner():
            while True:
                now = int(datetime.datetime.now().timestamp())
                expired = QRcode.objects.filter(endtime__lt=now)
                if expired.exists():
                    count = expired.count()
                    expired.delete()
                    print(f"[{timezone.now()}] Supprimé {count} QR codes expirés")
                time.sleep(1)  # toutes les secondes

        t = threading.Thread(target=cleaner, daemon=True)
        t.start()
