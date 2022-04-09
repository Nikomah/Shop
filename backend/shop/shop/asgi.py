
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

from store.consumer import StoreConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"store$", StoreConsumer.as_asgi()),
        ]))
})
