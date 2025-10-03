from django.shortcuts import render
from django.views.decorators.cache import never_cache
@never_cache
def qrcode_scan(request):
    return render(request, "qrcode_scan.html")

@never_cache
def qrcode_json(request):
    from django.http import JsonResponse
    from .models import QRcode
    """Renvoie tous les QR codes en JSON"""
    qrcodes = QRcode.objects.all().order_by("-timestamp")
    data = [
        {
            "id": qr.uuid,
            "data": qr.data,
            "creator": qr.creator,
            "timestamp": qr.timestamp,
            "qr": qr.qr.url if qr.qr else None,
        }
        for qr in qrcodes
    ]
    return JsonResponse(data, safe=False)

@never_cache
def qrcode_list(request):
    """Renvoie la page HTML avec le frontend"""
    return render(request, "qrcode_list.html")