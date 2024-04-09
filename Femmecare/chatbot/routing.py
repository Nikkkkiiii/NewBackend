from django.urls import path
from . import consumers

websoscket_urlpatterns = [
    path('ws/chat/<username_from>/<username_to>/', consumers.ChatbotConsumer.as_asgi()),
]