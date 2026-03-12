from django.urls import path
from messaging.views import index




urlpatterns = [
    path("message/", index, name="message")
]