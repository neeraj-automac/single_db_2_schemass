from django.urls import path
from. import consumers


print("routingggg")
websocket_urlpatterns=[
    path('mqtt_machine_app', consumers.ChatConsumer.as_asgi())

]




