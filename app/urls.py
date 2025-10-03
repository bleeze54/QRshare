from django.urls import path
from .views import *

urlpatterns = [path('scan', qrcode_scan, name='scan'),
    path("qrcodes/json", qrcode_json, name="qrcodes_json"),
    path("qrcodes", qrcode_list, name="qrcode_list"),
]

    