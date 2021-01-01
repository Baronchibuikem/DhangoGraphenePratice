from django.urls import re_path
from trips.consumers import TaxiConsumer


websocket_urlpatterns = [
    re_path(r'ws/taxi/$', TaxiConsumer.as_asgi()),
]
