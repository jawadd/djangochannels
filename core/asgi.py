import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import home.routing
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
   'http': get_asgi_application(),
   'websocket': AuthMiddlewareStack(
       URLRouter(
       home.routing.websocket_urlpatterns
   ))
}) 

