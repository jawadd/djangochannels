from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/wsc/',consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/',consumers.MyAsyncWebsocketConsumer.as_asgi()),

    # path('ws/sc/<str:groupkaname>/',consumers.MyWebsocketConsumer.as_asgi()),
    # path('ws/ac/<str:groupkaname>/',consumers.MyASyncConsumer.as_asgi()),
]