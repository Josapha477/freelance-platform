from django.conf import settings
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_sender")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_recipient")
    subject = models.CharField(max_length=100)
    body = models.TextField(default="")
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

