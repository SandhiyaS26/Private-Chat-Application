from django.urls import re_path
from chat_app import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/private/(?P<user1>\w+)/(?P<user2>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

