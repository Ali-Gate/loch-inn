import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from loch_inn import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loch_inn.settings')


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    }
)
