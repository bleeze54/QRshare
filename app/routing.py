from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/qr/$", consumers.QRConsumer.as_asgi()),
    re_path(r"ws/qrcodes/$", consumers.QRConsumer.as_asgi()),
]
