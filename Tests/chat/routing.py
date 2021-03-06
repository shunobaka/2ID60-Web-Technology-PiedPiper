from channels.routing import route
from .consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_add, path=r"^/chat/(?P<room_id>\d+)$"),
    route("websocket.receive", ws_message, path=r"^/chat/(?P<room_id>\d+)$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/chat/(?P<room_id>\d+)$"),
]